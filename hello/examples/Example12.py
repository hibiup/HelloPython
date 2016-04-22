#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

__author__ = 'Anonymous'

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# 更精确地控制枚举类型，可以从Enum派生出自定义类
# @unique装饰器可以帮助我们检查保证没有重复值。
@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

mon = Weekday.Mon
print(mon)
print(Weekday['Tue'])
print(Weekday.Tue)
print(Weekday.Tue.value)
print(Weekday(1))

for name, member in Weekday.__members__.items():
    print(name, '=>', member)

##################################
# 异常处理
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('except:', e)
except Exception as e:
    print('except:', e)
    raise e
else:
    print('unkonw error!')
    raise Exception('unkonw error!')
finally:
    print('finally...')

print('END')