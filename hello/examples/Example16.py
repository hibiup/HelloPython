#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

##############################################
# 多 CPU 问题
#
# 多核可以同时执行多个线程，一个死循环线程会100%占用一个CPU，如果有两个死循环线程，在多核CPU中，可以监控到会占用200%的CPU，也就是占用两个CPU核心。
# 但是 Python 启动与CPU核心数量相同的N个线程，比如在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。因为Python的线程虽然是真正的线程，但
# 解释器执行代码时，有一个GIL锁：Global Interpreter Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，
# 让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只
# 能用到1个核。GIL是Python解释器设计的历史遗留问题，所以，在Python中，可以使用多线程，但不要指望能有效利用多核。不过，也不用过于担心，Python虽然
# 不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。


######################################
# 新线程执行的代码:
import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


def mainThread():
    print('thread %s is running...' % threading.current_thread().name)

    # 创建新线程
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    # 将线程 join() 主线程后，主线程会等待子线程结束再继续执行，否则两个线程会平行执行
    t.join()

    print('thread %s ended.' % threading.current_thread().name)


mainThread()

######################################
# 线程锁
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()  # 建立一个锁


def change_it(n):
    # 申明引用全局变量
    global balance
    # 先存后取，结果应该为0:
    balance = balance + n
    balance = balance - n


def run_thread(n):
    print('thread %s is running...' % threading.current_thread().name)
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()


def mainThread():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)


mainThread()

######################################
# ThreadLocal 可以用于仅仅在当前线程方法间共享变量
import threading

# 创建全局 ThreadLocal 对象. 是然是全局的，但是存在其中的变量却是线程本地的
local_school = threading.local()


def process_student():
    # 从 ThreadLocal 获取当前线程关联的 student name
    stdName = local_school.student
    print('Hello, %s (in %s)' % (stdName, threading.current_thread().name))


def process_thread(stdName):
    # 将 name 绑定到 ThreadLocal 池中
    local_school.student = stdName
    # 将尝试在另一个方法中获取student name
    process_student()


def mainThread():
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')  # 线程A 的student name 是 Alice
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')    # 线程B 的student name 是 Bob
    t1.start()
    t2.start()
    t1.join()
    t2.join()


mainThread()
