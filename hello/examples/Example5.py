# Example5.py
# -*- coding: utf-8 -*-

##############################
## map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
#
# 先定义一个函数
def f(x):
    return x * x

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上
from functools import reduce

def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

# convert str to int
def str2int(str):
    def fn(x, y):
         return x * 10 + y
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    return reduce(fn, map(char2num, str))

print(str2int('13579'))

def str2int(str):
    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    return reduce(lambda x, y: x * 10 + y, map(char2num, str))          # lambda 语法，定义匿名闭包

print(str2int('2468'))

#######################################
## filter
#
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))