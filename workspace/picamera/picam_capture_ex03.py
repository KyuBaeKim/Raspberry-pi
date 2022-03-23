from time import sleep
from picamera import PiCamera

# EXLICITLY OPEN A NEW FILE CALLED MY_IMAGE.JPG
my_file = open('my_image.jpg', 'wb')

camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture(my_file)