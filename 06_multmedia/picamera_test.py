import picamera
import time

path = '/home/pi/src5/06_multmedia'

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480) #찍을때 1번만(사이즈 지정)
    camera.start_preview() #무조건 1번만
    time.sleep(3)          #카메라 준비시간
    #camera.capture("%s/photo.jpg" % path) #카메라 캡쳐
    camera.start_recording("%s/video.h264" % path)
    input('press enter to stop')
    camera.stop_recording

finally:
    camera.stop_preview() #무조건 1번만