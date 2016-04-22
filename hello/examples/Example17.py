#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

# 分布式多进程通过 Python 的 multiprocessing 把多进程分布到多台机器上。同时将进程间通讯的 Queue 暴露到网络上去，让其他机器的进程访问Queue来实现分布式进程间通讯

import queue
import random
import time
from multiprocessing.managers import BaseManager


# Python 的 multiprocessing 模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


#################################################
# 调度进程，运行在调度机上
#
class Manager(object):
    def run(self):
        # 发送消息的队列:
        task_queue = queue.Queue()
        # 接收结果的队列:
        result_queue = queue.Queue()

        # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
        QueueManager.register('get_task_queue', callable=lambda: task_queue)
        QueueManager.register('get_result_queue', callable=lambda: result_queue)
        # 绑定端口5000, 设置验证码'abc':
        manager = QueueManager(address=('', 5000), authkey=b'abc')
        # 启动Queue:
        manager.start()

        # 获得通过网络访问的Queue对象:
        task = manager.get_task_queue()
        result = manager.get_result_queue()

        # 通过 task 发送几个消息进去:
        for i in range(10):
            n = random.randint(0, 10000)
            print('Put task %d...' % n)
            task.put(n)

        # 从result队列读取结果:
        print('Try get results...')
        for i in range(10):
            r = result.get(timeout=10)
            print('Result: %s' % r)

        # 关闭:
        manager.shutdown()
        print('master exit.')


#################################################
# 工作进程，运行在其他机器上
#
class Worker(object):
    def run(self):
        # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
        QueueManager.register('get_task_queue')
        QueueManager.register('get_result_queue')

        # 连接到服务器，也就是运行task_master.py的机器:
        server_addr = '127.0.0.1'
        print('Connect to server %s...' % server_addr)
        # 端口和验证码注意保持与task_master.py设置的完全一致:
        m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
        # 从网络连接:
        m.connect()

        # 获取Queue的对象:
        task = m.get_task_queue()
        result = m.get_result_queue()

        # 从task队列取任务,并把结果写入result队列:
        for i in range(1000):
            try:
                n = task.get(timeout=1)
                print('run task %d * %d...' % (n, n))
                r = '%d * %d = %d' % (n, n, n * n)
                time.sleep(1)
                result.put(r)
            except queue.Queue.Empty:
                print('task queue is empty.')

        # 处理结束:
        print('worker exit.')


manager = Manager()
worker = Worker()

manager.run()
worker.run()
