from gpiozero import PWMLED
from time import sleep
led = PWMLED(13)

while True:
    led.Value = 0 # OFF
    sleep(1)
    led.Value = 0.5 # half brightness
    sleep(1)
    led.value = 1 # full brighteness
    sleep(1)