# Example2.py
# -*- coding: utf-8 -*-

## if
sum = input("100 + 200 = ")
if 100 + 200 == int(sum):
    print('100 + 200 =', sum)
else:
    print('Answer is', '300' == sum)

## for
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
     print(key)

# range 函数生成一个范围内的自然数
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

## while
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

