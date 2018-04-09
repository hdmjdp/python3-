import numpy as np
from datetime import datetime
import logging
import time
from threading import Thread
logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')
class CruiseBot(object):
    def __init__(self):
        self.name = 'Cruise'
        self._init_start_time()
    def cruise(self):
        self._main_loop()
    def _init_start_time(self):
        self.start_time = datetime.now().minute
    def _main_loop(self):
        # this is his main duty job
        while True:
            logging.debug('hello, I am {}, now time is: {}'.format(self.name, datetime.now()))
            time.sleep(5)
            now = datetime.now().minute
            if now - self.start_time == 1:
                # 1分钟之后开一个线程执行另外一个事情
                logging.debug('start execute job 1')
                t = Thread(name='alice', target=self._thread_job_1, args=(1,))
                t.start()
            # if now - self.start_time == 2:
            #     # 2分钟之后开一个线程执行另外一个事情
            #     logging.debug('start execute job 2')
            #     t = Thread(name='bob', target=self._thread_job_2, args=(2,))
            #     t.start()
    @staticmethod
    def _thread_job_1(i):
        while True:
            logging.debug('thread jobber {}, i am eating hamburg!!!!'.format(i))
            time.sleep(2)
    # @staticmethod
    # def _thread_job_2(i):
    #     while True:
    #         logging.debug('thread jobber {}, i am doing say hello'.format(i))
    #         time.sleep(2)


def add():
    return np.random.randint(0,10)

res = []
def thread_job_1(i):
    # while True:
    logging.debug('thread jobber {}, i am eating hamburg!!!!'.format(i))
    s = add()
    time.sleep(20)  # 执行时间
    res.append(s)


def main():
    start_time = datetime.now().second
    name = 'Cruise'
    while True:
        logging.debug('hello, I am {}, now time is: {}'.format(name, datetime.now()))
        time.sleep(5)
        now = datetime.now().second
        if (now - start_time) % 10:
            # 1分钟之后开一个线程执行另外一个事情
            logging.debug('start execute job 1')
            t = Thread(name='alice', target=thread_job_1, args=(1,))
            t.start()
            if res:
                print("got res:=======", res)

    # cruise_bot = CruiseBot()
    # cruise_bot.cruise()


if __name__ == '__main__':
    main()