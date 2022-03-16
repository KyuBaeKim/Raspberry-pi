from gpiozero import LED, Button
from signal import pause
led = LED(19)
button = Button(21)
led.source = button
pause()