from gpiozero import Button
from signal import pause

def say_hello():
    print("Hello!")

button = Button(21, bounce_time= 0.05)

button.when_pressed = say_hello

pause()