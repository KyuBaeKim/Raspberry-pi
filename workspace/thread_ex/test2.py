import time
from consumer import Consumer
from producer import Producer
from queue import Queue

def main():
    q = Queue(5)

    c = Consumer(q)
    p = Producer(q)

    c.start()
    p.start()

    time.sleep(10)


main()
# main 스레드 종료 시 daemon 스레드 자동 종료