
from gpiozero import PWMLED
from time import sleep
from signal import pause

led = PWMLED(13)

led.pulse()
pause()