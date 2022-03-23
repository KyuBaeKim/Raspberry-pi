from ast import arg
from asyncore import file_dispatcher
from net import send_file

ADDR = ('172.30.1.57', 1234)

files = [
    '/home/pi/workspace/Opencv/data/20220321_141309.mp4',
    '/home/pi/workspace/Opencv/data/20220314_174937.mp4',
    '/home/pi/workspace/Opencv/data/20220314_175019.mp4',
    '/home/pi/workspace/Opencv/data/20220317_135109.mp4'
]

# 방법 1
for file in files:
    send_file(ADDR, file)

print('=================================================')

# 방법 2 - 스레드 이용
from threading import Thread

for file in files:
    t = Thread(target=send_file, args=(ADDR, file))
    t.start()