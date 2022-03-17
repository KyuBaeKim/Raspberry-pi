from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(23, 24) # echo, trig

while True:
    print(f'Distance to nearest object is {sensor.distance:.3f} m')
    sleep(1)