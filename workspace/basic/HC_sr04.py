import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# 센서에 연결한 Trig와 Echo 핀의 친 번호 설정
TRIG = 24
ECHO = 23
print("Distance measurement in progress")

#Trig와 Echo 핀의 출력/입력 설정
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#Trig핀의 신호를 0으로 출력
GPIO.output(TRIG, False)
print("Waiting for sensor to settle")
time.sleep(2) # 신호 안정화를 위해 2초간 대기

try:
    while True:
        GPIO.output(TRIG, True) # Trigger 