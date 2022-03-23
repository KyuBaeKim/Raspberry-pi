# picamera 라이브러리 임포트
import picamera
# time 라이브러리 임포트
from time import sleep
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()

for i in range(5):
    sleep(5)
    camera.capture(f'/home/pi/image_{i}.jpg')

camera.stop_preview()