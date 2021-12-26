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
    # os.system('cd /root/Hikvision_camera/')
    # os.chdir('/home/zhny/Hikvision_camera/')  # 切换到指定的运行目录
    # print(os.getcwd())
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

    # 实例化camera
    # SONG
    cam1 = Camera(token1, 'G61903718', 1, 'No01L')
    cam2 = Camera(token1, 'G53497397', 1, 'No01S')
    cam3 = Camera(token1, 'G61903594', 1, 'No02L')
    cam4 = Camera(token1, 'G53497429', 1, 'No02S')
    cam5 = Camera(token1, 'G61903515', 1, 'No03L')
    cam6 = Camera(token1, 'G53497414', 1, 'No03S')
    cam7 = Camera(token1, 'G61903598', 1, 'No04L')
    cam8 = Camera(token1, 'G53497399', 1, 'No04S')
    cam9 = Camera(token1, 'G65260073', 1, 'No05L')
    cam10 = Camera(token2, 'G53497448', 1, 'No05S')
    cam11 = Camera(token1, 'G47462754', 1, 'No06S')
    cam12 = Camera(token2, 'G53497387', 1, 'No07S')
    cam13 = Camera(token2, 'F98676770', 1, 'No08S')
    cam14 = Camera(token2, 'G53497456', 1, 'No09S')
    cam15 = Camera(token2, 'G53497454', 1, 'No10S')

    # NKY
    cam16 = Camera(token2, 'G61903554', 1, 'SP01L')
    cam17 = Camera(token2, 'F27981779', 1, 'SP01S')
    cam18 = Camera(token2, 'F27981800', 1, 'SP02S')
    cam19 = Camera(token2, 'G61903542', 1, 'DL01L')

    cam20 = Camera(token3, 'F27981777', 1, 'DL02S')
    cam21 = Camera(token3, 'E88570011', 1, 'DS01S')
    cam22 = Camera(token3, 'E88569964', 1, 'DS02S')
    cam23 = Camera(token3, 'E88570024', 1, 'SH02S')
    cam24 = Camera(token3, 'E88570046', 1, 'SH01S')
    cam25 = Camera(token3, 'E88569979', 1, '44443')
    cam26 = Camera(token3, 'F27981765', 1, 'NKYXS')

    # 多进程
    p = Pool(8)  # 进程池
    #
    p.apply_async(getPhotoFruit, args=(cam1,))
    p.apply_async(getPhotoFruit, args=(cam19,))
    p.apply_async(getPhotoFruit, args=(cam2,))
    p.apply_async(getPhotoFruit, args=(cam18,))
    p.apply_async(getPhotoFruit, args=(cam3,))
    p.apply_async(getPhotoFruit, args=(cam17,))
    p.apply_async(getPhotoFruit, args=(cam4,))
    p.apply_async(getPhotoFruit, args=(cam16,))
    p.apply_async(getPhotoFruit, args=(cam5,))
    p.apply_async(getPhotoFruit, args=(cam15,))
    p.apply_async(getPhotoFruit, args=(cam6,))
    p.apply_async(getPhotoFruit, args=(cam14,))
    p.apply_async(getPhotoFruit, args=(cam7,))
    p.apply_async(getPhotoFruit, args=(cam13,))
    p.apply_async(getPhotoFruit, args=(cam8,))
    p.apply_async(getPhotoFruit, args=(cam12,))
    p.apply_async(getPhotoFruit, args=(cam9,))
    p.apply_async(getPhotoFruit, args=(cam10,))
    p.apply_async(getPhotoFruit, args=(cam11,))

    p.apply_async(getPhotoFruit, args=(cam20,))
    p.apply_async(getPhotoFruit, args=(cam21,))
    p.apply_async(getPhotoFruit, args=(cam22,))
    p.apply_async(getPhotoFruit, args=(cam23,))
    p.apply_async(getPhotoFruit, args=(cam24,))
    p.apply_async(getPhotoFruit, args=(cam25,))
    p.apply_async(getPhotoFruit, args=(cam26,))

    # # 关闭进程池
    p.close()
    p.join()

    # 单线程
    # getPhotoFruit(cam1)
    # # getPhotoFruit(cam2)
    # getPhotoFruit(cam3)
    # getPhotoFruit(cam4)
    # getPhotoFruit(cam5)
    # getPhotoFruit(cam6)
    # getPhotoFruit(cam7)
    # getPhotoFruit(cam8)
    # getPhotoFruit(cam9)
    # # getPhotoFruit(cam10)
    # # getPhotoFruit(cam11)
    # getPhotoFruit(cam12)
    # getPhotoFruit(cam13)
    # getPhotoFruit(cam14)
    # getPhotoFruit(cam15)
    # getPhotoFruit(cam16)
    # getPhotoFruit(cam17)
    # getPhotoFruit(cam18)
    # getPhotoFruit(cam19)
