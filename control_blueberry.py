from control import Camera, Account
from datetime import datetime
from multiprocessing import Pool
import os
import time
import requests


def getPhoto(cam, number):  # 批量调用getPhotograph方法
    for i in range(1, number + 1):
        cam.getPhotograph(i)


def getPhotoFruit(cam, a=1, b=3):  # 批量调用getPhotograph方法2
    for i in range(a, b + 1):
        # cam.getPhotographFruit(i)
        cam.getPhotograph(i)

class CameraBlue(Camera):
    def getPhotograph(self):  # 调用预置点并抓拍
        # 取消预置点
        # print('设备:' + self.camName + ' deviceSerial:' + self.deviceSerial + ' index:' + str(index))
        print('设备:' + self.camName + ' deviceSerial:' + self.deviceSerial)

        try:

            # 获取当前时间
            # 时间精确到小时
            Now = str(datetime.now())
            times = Now[:10] + '_' + Now[11:13] + '_' + Now[14:16]
            # times = Now[:10] + '_' + Now[11:13]
            # times2 = Now[:4] + Now[5:7] + Now[8:10] + Now[11:13] + Now[14:16]
            print(times)

            # 2022蓝莓无需调用预置点
            # 20210119修改为40秒
            # 调用预置点并等待40秒
            # self.point(index)
            # time.sleep(40)

            # 抓拍图片，返回图片的url
            url = self.photograph()
            print(url)

            # 保存图片到本地
            response = requests.get(url)
            img = response.content
            # imgName = './' + self.deviceSerial + '/' + str(index) + '_' + times + '.jpg'
            # imgName = './' + self.deviceSerial + '/' + str(index) + times2 + '.jpg'
            imgName = './' + self.camName + '/' + times + '.jpg'
            print(imgName)

            # if os.path.exists(self.deviceSerial) == False:  # 查看是否有文件夹
            if os.path.exists(self.camName) == False:  # 查看是否有文件夹
                os.mkdir(self.camName)
            with open(imgName, 'wb') as f:
                f.write(img)

        except BaseException as e:
            print('error!')
            print(e)

if __name__ == '__main__':
    # os.chdir('/home/zhny/Hikvision_camera/')  # 切换到指定的运行目录
    print(os.getcwd())
    print(datetime.now())

    # 获取token4
    no = 'No4'
    access4 = Account(no)
    token4 = access4.getAccessToken()
    print(token4)

    # 实例化camera
    cam1 = CameraBlue(token4, 'G08917948', 1, 'LM01')
    cam2 = CameraBlue(token4, 'G08917830', 1, 'LM02')
    cam3 = CameraBlue(token4, 'G61903543', 1, 'LM03')

    #拍照
    cam1.getPhotograph()
    cam2.getPhotograph()
    cam3.getPhotograph()



