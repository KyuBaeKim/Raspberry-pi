import time
from picamera import PiCamera
import numpy as np
import cv2
import time

with PiCamera() as camera:
    camera.resolution = (640, 480)

    image= np.empty((480, 640, 3), dtype=np.uint8)

    start = time.time()
    camera.capture(image, 'bgr')
    cv2.imshow('frame', image)
    end = time.time()
    fps = 1/(end-start)
    print(f'fps: {fps:.2}')
    
    cv2.waitKey(0)