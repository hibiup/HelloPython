# Example4.py
# -*- coding: utf-8 -*-

##############################################
## 列表生成式
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

## 用 列表生成式 达到同样效果
L = [x * x for x in range(1, 11)]
print(L)
# 带条件
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)
# 二重循环
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 列目录
import os
print([d for d in os.listdir('.')])

## enum type. enum 会返回 index
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# for 可以作用于多个成员的变量，例如 dict
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

# 因此for应用于列表生成式会有一些特殊简化的效果
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

# lower case letters
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

##############################################
## 生成器
## 但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
## 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，
## 称为生成器（Generator）。要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
#
g = (x * x for x in range(10))  # 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。
print(next(g))

for n in g:
    print(n)

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
fib(10)

# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield  b         # key word “yield" means this is a generator, function will return and continue from here.
        a, b = b, a + b
        n = n + 1

for n in fib(10):
    print(n)

# 进一步理解 yield
def odd():
    print('next() 1:')
    yield 1
    print('next() 2:')
    yield 3
    print('next() 3:')
    yield 5

o = odd()
print(o.__next__())
print(o.__next__())
print(o.__next__())