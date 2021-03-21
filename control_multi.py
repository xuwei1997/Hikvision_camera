from control import Camera, Account, getKey
from datetime import datetime
from multiprocessing import Pool
import os
import time


# def getPhotoMul(cam,inx):
#     cam.getPhotograph(inx)


def getPhoto(cam, number):
    for i in range(1, number + 1):
        cam.getPhotograph(i)

def getPhotoFruit(cam, a,b):
    for i in range(a, b + 1):
        cam.getPhotographFruit(i)
        # cam.getPhotograph(i)


if __name__ == '__main__':
    # os.system('cd /root/Hikvision_camera/')
    os.chdir('/root/Hikvision_camera/')
    print(os.getcwd())
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

    p = Pool(4)

    p.apply_async(getPhoto, args=(cam1, 11))
    p.apply_async(getPhoto, args=(cam2, 7))
    p.apply_async(getPhoto, args=(cam3, 10))
    p.apply_async(getPhoto, args=(cam4, 10))
    p.apply_async(getPhoto, args=(cam5, 8))
    p.apply_async(getPhoto, args=(cam6, 10))
    #
    time.sleep(120)
    p.apply_async(getPhotoFruit, args=(cam1, 12,30))
    p.apply_async(getPhotoFruit, args=(cam2, 8, 13))
    p.apply_async(getPhotoFruit, args=(cam5, 9, 10))
    p.apply_async(getPhotoFruit, args=(cam6, 11, 15))


    p.close()
    p.join()
