import RPi.GPIO as GPIO
import time

count = 0;
# button_callback 함수를 정의합니다.
def button_callback(channel):
    global count 
    count += 1
    print(count, "Button pushed!")
    

    

# 사용할 GPIO피의 번호를 선정ㅎ바니다.
button_pin = 21



# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 IN?OUT 설정 , PULL UP 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Event 방식으로 핀의 Rising 신호를 감지하면 button_callback 함수를 실행합니다.
GPIO.add_event_detect(button_pin,GPIO.RISING,callback = button_callback,bouncetime = 300)

try:
    while 1:
        time.sleep(0.1) #0.1초 딜레이
        
except:
    GPIO.cleanup() 