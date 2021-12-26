import requests
import time
import os
from datetime import datetime


def getPhotoFruit(cam, a=1, b=3):  # 批量调用getPhotograph方法2
    for i in range(a, b + 1):
        # cam.getPhotographFruit(i)
        cam.getPhotograph(i)

class Account(object):  # 账户类，获取摄像头控制权限
    def __init__(self, no):
        self.con_file_path = 'config' + no + '.txt'
        self.token_file_path = 'token' + no + '.txt'
        self.appKey = None
        self.appSecret = None
        self.getKey()

    def getKey(self):  # 获取key
        with open(self.con_file_path, 'r') as f:
            Key = f.read()
            Key = eval(Key)
            print(Key)
            self.appKey = Key['appKey']
            self.appSecret = Key['appSecret']

            # return (Key['appKey'], Key['appSecret'])

    def getAccessTokenAPI(self):  # 从API读取Token
        data = {'appKey': self.appKey, 'appSecret': self.appSecret}
        r = requests.post('https://open.ys7.com/api/lapp/token/get', data=data)
        text = r.json()
        # print('code:'+text['code'])
        print(text)

        if text['code'] == '200':
            # 组建写入文件的json
            output = {'accessToken': text['data']['accessToken'], 'expireTime': text['data']['expireTime']}
            output = str(output)
            # 写入文件
            # f = open(self.token_file_path, 'w')
            # f.write(output)
            # f.close()

            # 写入文件
            with open(self.token_file_path, 'w')as f:
                f.write(output)

            print(output)
            return text['data']['accessToken']

    def getAccessToken(self):  # 读取Token
        if os.path.exists(self.token_file_path):  # 文件在，则读文件获取Token
            with open(self.token_file_path, 'r') as f:
                text = f.read()
            text = eval(text)
            t = time.time()
            nowTime = int(round(t * 1000))  # 毫秒级时间戳
            remainTime = text['expireTime'] - nowTime
            # print(remainTime)
            if remainTime > 86400000:
                return text['accessToken']
            else:
                return self.getAccessTokenAPI()
        else:
            return self.getAccessTokenAPI()


class Camera(object):
    def __init__(self, accessToken, deviceSerial, channelNo, camName):
        self.accessToken = accessToken
        self.deviceSerial = deviceSerial
        self.channelNo = channelNo
        self.camName = camName

    def point(self, index):  # 调用预置点，使摄像头转动到预置点的方向
        print('调用预置点:' + self.camName + ' index:' + str(index))
        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo,
                'index': index}
        r = requests.post('https://open.ys7.com/api/lapp/device/preset/move', data=data)
        text = r.json()
        print(self.camName + '_point_code:' + text['code'])
        # print(text)

    def focusing(self):  # 聚焦
        print("focusing")
        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo,
                'direction': 10, 'speed': 1}
        r = requests.post('https://open.ys7.com/api/lapp/device/ptz/start', data=data)
        text = r.json()
        print(text)
        time.sleep(10)
        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo,
                'direction': 10, 'speed': 1}
        r = requests.post('https://open.ys7.com/api/lapp/device/ptz/stop', data=data)
        text = r.json()
        print(text)

    def photograph(self):  # 抓拍当前角度图片，返回图片的url
        print('抓拍图片，返回图片的url:' + self.camName)
        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo}
        r = requests.post('https://open.ys7.com/api/lapp/device/capture', data=data)
        text = r.json()
        print(self.camName + '_photograph_code:' + text['code'])
        # print(text)
        return text['data']['picUrl']

    def getPhotograph(self, index):  # 调用预置点并抓拍
        print('设备:' + self.camName + ' deviceSerial:' + self.deviceSerial + ' index:' + str(index))
        try:

            # 获取当前时间
            # 时间精确到小时
            Now = str(datetime.now())
            # times = Now[:10] + '_' + Now[11:13] + '_' + Now[14:16]
            times = Now[:10] + '_' + Now[11:13]
            # times2 = Now[:4] + Now[5:7] + Now[8:10] + Now[11:13] + Now[14:16]
            # print(times)

            # 20210119修改为40秒
            # 调用预置点并等待40秒
            self.point(index)
            time.sleep(40)

            # 抓拍图片，返回图片的url
            url = self.photograph()
            print(url)

            # 保存图片到本地
            response = requests.get(url)
            img = response.content
            # imgName = './' + self.deviceSerial + '/' + str(index) + '_' + times + '.jpg'
            # imgName = './' + self.deviceSerial + '/' + str(index) + times2 + '.jpg'
            imgName = './' + self.camName + '/' + str(index) + '_' + times + '.jpg'
            print(imgName)

            # if os.path.exists(self.deviceSerial) == False:  # 查看是否有文件夹
            if os.path.exists(self.camName) == False:  # 查看是否有文件夹
                os.mkdir(self.camName)
            with open(imgName, 'wb') as f:
                f.write(img)

        except BaseException as e:
            print('error!')
            print(e)

    def getPhotographFruit(self, index):  # 调用预置点并抓拍樱桃，添加了一步对焦到前景
        print('设备:' + self.camName + ' deviceSerial:' + self.deviceSerial + ' index:' + str(index))
        try:

            # 获取当前时间
            # 时间精确到小时
            Now = str(datetime.now())
            times = Now[:10] + '_' + Now[11:13]

            # 调用预置点并等待60秒
            self.point(index)
            time.sleep(60)
            # #聚焦,暂时取消
            # self.focusing()

            # 抓拍图片，返回图片的url
            url = self.photograph()
            print(url)

            # 保存图片到本地
            response = requests.get(url)
            img = response.content
            imgName = './' + self.deviceSerial + '/' + str(index) + '_' + times + '.jpg'
            if os.path.exists(self.deviceSerial) == False:  # 查看是否有文件夹
                os.mkdir(self.deviceSerial)
            with open(imgName, 'wb') as f:
                f.write(img)

        except BaseException as e:
            print('error!')


# def getKey(PATH):
#     with open(PATH, 'r') as f:
#         Key = f.read()
#         Key = eval(Key)
#         print(Key)
#         return (Key['appKey'], Key['appSecret'])


if __name__ == '__main__':
    print(datetime.now())

    # 获取token1
    no = 'No1'
    access1 = Account(no)
    token1 = access1.getAccessToken()
    print(token1)

    # 获取token2
    no = 'No2'
    access2 = Account(no)
    token2 = access2.getAccessToken()
    print(token2)

    # 获取token3
    no = 'No3'
    access3 = Account(no)
    token3 = access3.getAccessToken()
    print(token3)

    cam21 = Camera(token3, 'E88570011', 1, 'DS01S')

    getPhotoFruit(cam21)
