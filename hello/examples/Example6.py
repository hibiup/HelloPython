# Example6.py
# -*- coding: utf-8 -*-

########################################
## 函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

f = calc_sum(1, 3, 5, 7, 9)
print(f)           # f 等于返回值

# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f()) # f是函数，调用时才得到返回值

##
# 闭包没有及时处理共享变量的情况
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)     # 循环了三次，i 最终成了 3, 但是 fs中并没有逐次压入 i 每次的变化，而是压入函数 f，而函数 f 并没有及时处理 i，所以等到 count真正需要打印 fs时，函数 f 3次都是对 1=3做处理
    return fs
count1, count2, count3 = count()
print(count1())
print(count2())
print(count3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))   # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
count1, count2, count3 = count()
print(count1())
print(count2())
print(count3())

