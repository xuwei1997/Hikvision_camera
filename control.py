import requests
import time
import os
from datetime import datetime


class Account(object):
    def __init__(self, appKey, appSecret):
        self.appKey = appKey
        self.appSecret = appSecret

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
            # f = open('Token.txt', 'w')
            # f.write(output)
            # f.close()

            # 写入文件
            with open('Token.txt', 'w')as f:
                f.write(output)

            print(output)
            return text['data']['accessToken']

    def getAccessToken(self):  # 读取Token
        if os.path.exists('Token.txt'):  # 文件在，则读文件获取Token
            with open('Token.txt', 'r') as f:
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

    def point(self, index):  # 调用预置点
        print('调用预置点:' + self.camName + ' index:' + str(index))
        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo,
                'index': index}
        r = requests.post('https://open.ys7.com/api/lapp/device/preset/move', data=data)
        text = r.json()
        print('code:' + text['code'])
        # print(text)

    def photograph(self):  # 抓拍图片，返回图片的url
        print('抓拍图片，返回图片的url:'+ self.camName)
        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo}
        r = requests.post('https://open.ys7.com/api/lapp/device/capture', data=data)
        text = r.json()
        print('code:' + text['code'])
        # print(text)
        return text['data']['picUrl']

    def getPhotograph(self, index):  # 调用预置点并抓拍
        print('设备:' + self.camName + ' deviceSerial:' + self.deviceSerial + ' index:' + str(index))
        try:

            # 获取当前时间
            Now = str(datetime.now())
            times = Now[:10] + '_' + Now[11:13] + '_' + Now[14:16]
            # print(times)

            # 调用预置点并等待30秒
            self.point(index)
            time.sleep(30)

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


def getKey():
    with open('config.txt', 'r') as f:
        Key = f.read()
        Key = eval(Key)
        print(Key)
        return (Key['appKey'], Key['appSecret'])


if __name__ == '__main__':
    print(datetime.now())

    appKey, appSecret = getKey()
    access = Account(appKey, appSecret)
    Token = access.getAccessToken()
    print(Token)

    cam1 = Camera(Token, 'F03210481', 1, '设备1')
    cam2 = Camera(Token, 'E88569964', 1, '设备2')
    cam3 = Camera(Token, 'E88569979', 1, '设备3')
    cam4 = Camera(Token, 'E88570024', 1, '设备4')
    cam5 = Camera(Token, 'E88570011', 1, '设备5')
    cam6 = Camera(Token, 'E88570046', 1, '设备6')

    cam1.getPhotograph(1)
    cam1.getPhotograph(2)
    cam1.getPhotograph(3)
    cam1.getPhotograph(4)
    cam1.getPhotograph(5)
    cam1.getPhotograph(6)
    cam1.getPhotograph(7)
    cam1.getPhotograph(8)
    cam1.getPhotograph(9)

    cam2.getPhotograph(1)
    cam2.getPhotograph(2)
    cam2.getPhotograph(3)
    cam2.getPhotograph(4)
    cam2.getPhotograph(5)
    cam2.getPhotograph(6)

    cam3.getPhotograph(1)
    cam3.getPhotograph(2)
    cam3.getPhotograph(3)
    cam3.getPhotograph(4)
    cam3.getPhotograph(5)
    cam3.getPhotograph(6)
    cam3.getPhotograph(7)

    cam4.getPhotograph(1)
    cam4.getPhotograph(2)
    cam4.getPhotograph(3)
    cam4.getPhotograph(4)
    cam4.getPhotograph(5)
    cam4.getPhotograph(6)
    cam4.getPhotograph(7)
    cam4.getPhotograph(8)
    cam4.getPhotograph(9)

    cam5.getPhotograph(1)
    cam5.getPhotograph(2)
    cam5.getPhotograph(3)
    cam5.getPhotograph(4)
    cam5.getPhotograph(5)
    cam5.getPhotograph(6)

    # cam6.getPhotograph(1)
    # cam6.getPhotograph(2)
    # cam6.getPhotograph(3)
    # cam6.getPhotograph(4)
    # cam6.getPhotograph(5)
