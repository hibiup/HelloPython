# Example8.py
# -*- coding: utf-8 -*-

def hello(name, greeting):
    print(greeting, name)

hello("Jeff", "Hello")

# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数。第一个参数是函数名，后面是参数默认值
import functools
hello2 = functools.partial(hello, greeting="Hello")
hello2("WangJi")

hello3 = functools.partial(hello, name ="my lord", greeting="Hello")
hello3()