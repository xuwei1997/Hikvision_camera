from control import Camera, Account, getKey
from datetime import datetime
from multiprocessing import Pool
import os


# def getPhotoMul(cam,inx):
#     cam.getPhotograph(inx)


def getPhoto(cam, number):
    for i in range(1, number + 1):
        cam.getPhotograph(i)


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

    p.apply_async(getPhoto, args=(cam1, 9))
    p.apply_async(getPhoto, args=(cam2, 6))
    p.apply_async(getPhoto, args=(cam3, 7))
    p.apply_async(getPhoto, args=(cam4, 9))
    p.apply_async(getPhoto, args=(cam5, 6))
    p.apply_async(getPhoto, args=(cam6, 7))

    p.close()
    p.join()
