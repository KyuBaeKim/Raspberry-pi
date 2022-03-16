import RPi.GPIO as GPIO
import time

# 초록색 LED, 빨간색 LED, 센서 입력된 번호 설정
led_R = 16
led_G = 20
sensor = 12

GPIO.setmode(GPIO.BCM)

# LED 핀의 IN/OUT (입력/출력) 설정
GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_G, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

print("PIR Ready . . . . ")
time.sleep(5) # PIR 센서 준비 시간

try:
    while True:
        if GPIO.input(sensor) == 1: # 센서가 High(1) 출력
            GPIO.output(led_G, 1)
            GPIO.output(led_R, 0)
            print("Motion Detected")
            time.sleep(0.2)

        if GPIO.input(sensor) == 0: # 센서가 LOW(0) 출력
            GPIO.output(led_R, 1)
            GPIO.output(led_G, 0)
            time.sleep(0.2)
except KeyboardInterrupt:
    print("stopped by User")
    GPIO.cleanup()
