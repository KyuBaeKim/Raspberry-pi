from net import send_file

ADDR = ('172.30.1.57', 1234)
FILE_PATH = "/home/pi/workspace/Opencv/data/vtest.avi"


send_file(ADDR, FILE_PATH)