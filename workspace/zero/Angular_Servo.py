from gpiozero import AngularServo
from time import sleep

servo = AngularServo( 14, min_angle = -90, max_angle = 90, min_pulse_width = 0.0004, max_pulse_width=0.0024)


while True:
    servo.angle = -90
    sleep(2)
    servo.angle = 0
    sleep(2)
    servo.angle = 90
    sleep(2)
    servo.angle = 0
    sleep(2)