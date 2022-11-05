#!/usr/bin/python
'''
多线程的创建
two ways to create thread instance
1. threading.Thread 类直接创建
2. 继承 threading.Thread 类， 并且覆写run 方法
'''

import threading
from time import sleep


class Target:
    COUNT = 0
    LOCK = threading.Lock()
    COND = threading.Condition(LOCK)  # 条件变量需要绑定到互斥量
    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        cls.LOCK.acquire()
        if cls.INSTANCE is None:
            cls.INSTANCE = super().__new__(cls, *args, **kwargs)
        cls.LOCK.release()
        return cls.INSTANCE

    @classmethod
    def producer(cls, *args, **kwargs):
        while True:
            cls.COND.acquire()
            cls.COUNT += 1
            print("produce count=", cls.COUNT)
            if cls.COUNT % 5 == 0:
                cls.COND.notify()
            cls.COND.release()
            sleep(1)

    @classmethod
    def consumer(cls, *args, **kwargs):
        while True:
            cls.COND.acquire()
            while cls.COUNT % 5 != 0:
                cls.COND.wait()  # auto release
            print("*consumer count=", cls.COUNT)
            cls.COND.release()  # must release
            sleep(1)


class MyThread(threading.Thread):

    def run(self):
        print("run my thread")


if __name__ == "__main__":
    tar = Target()
    t = MyThread()
    t.start()
    t1 = threading.Thread(target=tar.producer)
    t2 = threading.Thread(target=tar.consumer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()