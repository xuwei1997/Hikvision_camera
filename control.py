import requests
import time
import os

class Account(object):
    def __init__(self,appKey,appSecret):
        self.appKey=appKey
        self.appSecret=appSecret

    def getAccessTokenAPI(self):#从API读取Token
        data={'appKey':self.appKey,'appSecret':self.appSecret}
        r=requests.post('https://open.ys7.com/api/lapp/token/get',data=data)
        text=r.json()
        # print('code:'+text['code'])
        print(text)

        if text['code']=='200':

            #组建写入文件的json
            output={'accessToken':text['data']['accessToken'],'expireTime':text['data']['expireTime']}
            output=str(output)
            #写入文件
            f = open('Token.txt', 'w')
            f.write(output)
            f.close()
            print(output)
            return text['data']['accessToken']

    def getAccessToken(self):#读取Token
        if os.path.exists('Token.txt'):#文件在，则读文件获取Token
            with open('Token.txt', 'r') as f:
                text=f.read()
            text=eval(text)
            t = time.time()
            nowTime=int(round(t * 1000))    #毫秒级时间戳
            remainTime=text['expireTime']-nowTime
            # print(remainTime)
            if remainTime>86400000:
                return text['accessToken']
            else:
                return self.getAccessTokenAPI()
        else:
            return self.getAccessTokenAPI()



class Camera(object):
    def __init__(self,accessToken,deviceSerial,channelNo):
        self.accessToken = accessToken
        self.deviceSerial = deviceSerial
        self.channelNo = channelNo

    def point(self,index): #调用预置点
        data = {'accessToken': self.accessToken,'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo, 'index': index}
        r = requests.post('https://open.ys7.com/api/lapp/device/preset/move',data=data)
        text = r.json()
        print('code:'+text['code'])
        print(text)

    def photograph(self): #抓拍图片
        data= {'accessToken': self.accessToken,'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo}
        r = requests.post('https://open.ys7.com/api/lapp/device/capture',data=data)
        text = r.json()
        print('code:' + text['code'])
        print(text)
        return text['data']['picUrl']

    def GetPhotograph(self,index):#调用预置点并抓拍
        print('deviceSerial:'+self.deviceSerial+' index:'+str(index))
        self.point(index)
        time.sleep(30)
        url=self.photograph()
        print(url)


def getKey():
    with open('config.txt', 'r') as f:
        Key = f.read()
        Key=eval(Key)
        print(Key)
        return (Key['appKey'],Key['appSecret'])


if __name__ == '__main__':
    appKey,appSecret=getKey()
    access=Account(appKey,appSecret)
    Token=access.getAccessToken()
    print(Token)

