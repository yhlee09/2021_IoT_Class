#카메라 = 

import picamera
import time

path = '/home/pi/src5/06_multmedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480) #찍을때 1번만(사이즈 지정)
    camera.start_preview() #무조건 1번만
    time.sleep(3)          #카메라 준비시간
    
    while(1):
        a = input('photo:1, video:2, exit:9 ')
        if a=='1':
            print("사진 촬영")
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.capture("%s/photo%s.jpg" % (path,now_str)) #카메라 캡쳐
        elif a=='2':
            print("동영상 촬영")
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording("%s/video_%s.h264" % (path,now_str)) #동영상 촬영
            input('press enter to stop')
            camera.stop_recording()
        elif a=='9':
            break
        else:
            print("wrong access")

finally:
    camera.stop_preview() #무조건 1번만

    
