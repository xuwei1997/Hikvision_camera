from control import Camera, Account
from datetime import datetime
from multiprocessing import Pool
import os
import time
# from control_blueberry import CameraBlue
import requests


def getPhoto(cam, number):  # 批量调用getPhotograph方法
    for i in range(1, number + 1):
        cam.getPhotograph(i)


def getPhotoFruit(cam, a=1, b=3):  # 批量调用getPhotograph方法2
    for i in range(a, b + 1):
        # cam.getPhotographFruit(i)
        cam.getPhotograph(i)

class CameraCra(Camera):
    def getPhotograph(self, index):  # 调用预置点并抓拍
        print('设备:' + self.camName + ' deviceSerial:' + self.deviceSerial + ' index:' + str(index))
        try:

            # 获取当前时间
            # 时间精确到分钟
            Now = str(datetime.now())
            times = Now[:10] + '_' + Now[11:13] + '_' + Now[14:16]
            print(times)

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


if __name__ == '__main__':
    # os.chdir('/home/zhny/Hikvision_camera/')  # 切换到指定的运行目录
    print(os.getcwd())
    print(datetime.now())

    # 获取token1
    no = 'No1'
    access1 = Account(no)
    token1 = access1.getAccessToken()
    print(token1)

    # # 获取token2
    # no = 'No2'
    # access2 = Account(no)
    # token2 = access2.getAccessToken()
    # print(token2)
    #
    # # 获取token3
    # no = 'No3'
    # access3 = Account(no)
    # token3 = access3.getAccessToken()
    # print(token3)

    # 实例化camera
    # SONG
    cam1 = CameraCra(token1, 'G61903718', 1, 'No01LC')

    # 多进程
    p = Pool(4)  # 进程池
    #
    p.apply_async(getPhotoFruit, args=(cam1, 4, 9))

    # # 关闭进程池
    p.close()
    p.join()
