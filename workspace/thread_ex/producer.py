from threading import Thread
import random
import time

class Producer(Thread):
    def __init__(self, queue):
        super().__init__()
        self.daemon = True
        self.queue = queue
        self.count = 0


    def producer(self):
        # 생산에 걸리는 지연시간
        delay = random.uniform(0.5 , 3)
        time.sleep(delay)

        self.count += 1
        msg = self.count
        print('Producer produce', msg)
        self.queue.put(msg) # 내가 만든 데이터를 큐에다가 넣는다.

    def run(self):
        while True:
            self.producer()