from gpiozero import LED
from signal import pause
red = LED(16)
red.blink(on_time= 0.5, off_time= 0.5 ,background=True) # 스레드로 동작하고 있다

print('-----------')

pause() # cpu 를 더이상 사용 안하게 만든다.

# while True: <- busy waiting
