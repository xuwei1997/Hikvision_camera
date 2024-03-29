# 拍摄全景图片
from control import Camera, Account, getKey
import requests
import time
from datetime import datetime
import os

class Camera_glo(Camera):#继承Camera类
    def move(self, direction, sec,speed=1):  # 输入移动的方向和秒，使摄像头转动到特定角度
        print('移动:' + self.camName + ' 方向:' + str(direction))

        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo,
                'direction': direction, 'speed': speed}
        r = requests.post('https://open.ys7.com/api/lapp/device/ptz/start', data=data)
        text = r.json()
        print(text)

        time.sleep(sec)

        data = {'accessToken': self.accessToken, 'deviceSerial': self.deviceSerial, 'channelNo': self.channelNo,
                'direction': direction, 'speed': 1}
        r = requests.post('https://open.ys7.com/api/lapp/device/ptz/stop', data=data)
        text = r.json()
        print(text)

    def getGlobalPhotograph(self):#抓拍全方位的图片
        #获取时间
        Now = str(datetime.now())
        times = Now[:10] + '_' + Now[11:13]+'_'+Now[14:16]
        print(times)

        # 初始化：右下角000开始，最大焦距
        self.move(8, 5)
        self.move(7,30,2)

        #开始抓拍
        for u in range(1,16):#up
            for l in range(1,17):#left
                print(str(u)+'_'+str(l))
                time.sleep(6)

                #保存图片到本地
                try:
                    url = self.photograph()
                    response = requests.get(url)
                    img = response.content
                    imgName = './' +times+ self.deviceSerial +'/'+ str(u)+'_'+str(l)+'.jpg'
                    if os.path.exists(times+ self.deviceSerial) == False:  # 查看是否有文件夹
                        os.mkdir(times+self.deviceSerial)
                    with open(imgName, 'wb') as f:
                        f.write(img)
                except BaseException as e:
                    print('error!')
                time.sleep(4)

                #转动
                self.move(2, 2.3)
                time.sleep(3)
                # self.move(10, 5)

            #回到最右000
            time.sleep(3)
            self.move(3,30,2)
            time.sleep(0.5)

            #向上
            self.move(0,4)
            time.sleep(0.5)

    def getPhotographPoint(self,x,y,homing=False):#抓拍特定角度图片
        # 初始化：右下角000开始，最大焦距
        if homing:
            self.move(8, 5)
            self.move(7, 15, 2)
            time.sleep(2)

        #转动
        self.move(2, (y-1)*2.3)
        self.move(0,(x-1)*4)
        self.move(10, 5)
        time.sleep(3)

        #拍照
        try:
            url = self.photograph()
            response = requests.get(url)
            img = response.content
            imgName = './' + self.deviceSerial + '/' + str(x) + '_' + str(y) + '.jpg'
            if os.path.exists(self.deviceSerial) == False:  # 查看是否有文件夹
                os.mkdir(self.deviceSerial)
            with open(imgName, 'wb') as f:
                f.write(img)
        except BaseException as e:
            print('error!')
        #归位
        self.move(7, 20, 2)






if __name__ == '__main__':
    appKey, appSecret = getKey()
    access = Account(appKey, appSecret)
    Token = access.getAccessToken()
    print(Token)

    cam4 = Camera_glo(Token, 'E88570024', 1, '设备4')
    # cam4.getGlobalPhotograph()

    cam4.getPhotographPoint(2,5)
