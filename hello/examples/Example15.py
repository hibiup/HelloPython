#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

###################################
# 依靠 Unix 操作系统建立多进程
import os

print('Process (%s) start...' % os.getpid())

# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

###################################
# 创建一个Process实例，用start()方法启动
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())

    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()  # join() 方法可以让主进程等待子进程结束后再继续往下运行。

    print('Child process end.')

###################################
# 进程池
from multiprocessing import Pool
import os, time, random

# 进程方法
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)

    # 将进程方法逐个加入池中
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')


###################################
# 外部子进程: 子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 如果子进程还需要输入，则可以通过communicate()方法输入：
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)

#####################################
# 进程间通信
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    # 发送三个字符
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    # 进程死循环,不断读取发送过来的消息
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建 Queue 用于进程间通讯，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()

    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()