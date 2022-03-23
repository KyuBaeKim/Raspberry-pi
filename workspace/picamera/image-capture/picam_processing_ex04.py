import time
from picamera import PiCamera
import numpy as np
import cv2

# bgr 배열을 jpg로 변환
def to_jpg(frame, quality = 80):
    encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),quality]
    is_success, jpg = cv2.imencode(".jpg", frame, encode_param)
    data = jpg.tobytes() # numpy 배열을 일반 python byte배열로 변환
    return data

with PiCamera() as camera:
    camera.resolution = (640,480)

    image = np.empty((480, 640, 3), dtype=np.uint8)

    while True:
        camera.capture(image, 'bgr', use_video_port=True)
        cv2.imshow('frame', image)

        # 이미지를 jpg로 변환
        jpg = to_jpg(image)
        # jpg를 네트워크로 전환

        if cv2.waitKey(1) ==27: # esc 키 입력시 종료
            break