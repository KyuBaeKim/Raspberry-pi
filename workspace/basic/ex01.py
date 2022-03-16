import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다. (BCM 모드)
led_pin = 16 #GPIO16

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# LED 핀의 IN/OUT 설정
GPIO.setup(led_pin, GPIO.OUT)

# 10번 반복문
try:
    for i in range(10):
        GPIO.output(led_pin,1) # LED ON
        time.sleep(1)          # 1초동안 대기상태
        GPIO.output(led_pin,0) # LED OFF
        time.sleep(1)          # 1초동안 대기상태
except:
    GPIO.cleanup()             # GPIO
