from control import Camera, Account
from datetime import datetime
from multiprocessing import Pool
import os
import time


def getPhoto(cam, number):  # 批量调用getPhotograph方法
    for i in range(1, number + 1):
        cam.getPhotograph(i)


def getPhotoFruit(cam, a=1, b=3):  # 批量调用getPhotograph方法2
    for i in range(a, b + 1):
        # cam.getPhotographFruit(i)
        cam.getPhotograph(i)


if __name__ == '__main__':
    os.chdir('/home/zhny/Hikvision_camera/')  # 切换到指定的运行目录
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
    cam1 = Camera(token1, 'G61903718', 1, 'No01LC')

    # 多进程
    p = Pool(4)  # 进程池
    #
    p.apply_async(getPhotoFruit, args=(cam1, 4, 9))

    # # 关闭进程池
    p.close()
    p.join()
