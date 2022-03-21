from termios import TIOCPKT_FLUSHREAD
import threading
from time import sleep

def sum(low, high):
    total = 0
    for i in range(low, high):
        total += 1
    print("Subthread", total)

t = threading.Thread(target = sum, args=(1, 100000))

t.start()

sleep(2)
print("Main Thread")