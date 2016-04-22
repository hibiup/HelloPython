# Example3.py
# -*- coding: utf-8 -*-

## return something
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-1))

## Doing nothing, if older then 18
def nop(age):
    if age >= 18:
        pass

#################################
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
# 其实返回的是一个 tuple!
r = move(100, 100, 60, math.pi / 6)
print(r)

##  可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1))
print(calc(1,2))
print(calc(1,2,3))

## "**"开头的参数是"关键字参数", 表示参数必须带有关键字(key)
# 关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, *age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30, city='Beijing',gender='M', job='Engineer')

