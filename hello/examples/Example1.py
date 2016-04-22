# Example1.py
# -*- coding: utf-8 -*-

print('hello, Python!', 'hello, World!', 'and hello my lord!')
print('I\'m Python.', '''I'm Python.''', "I'm Python!")
print("TRUE =", True, " FALSE =", False, " !TRUE = ", not True,  " !FALSE =", not False)

# Unicode
print('中', u'中', u'中'.encode('utf-8'), u'\u4e2d', u'A', u'\u0041')

# Variable
print( 'Hi, %s, you have $%d.' % ('Michael', 1000000))
print( '%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print(u'Hi, %s' % u'中国')
print('growth rate: %d%%' % 7)

# List
classmates = ['Bob', 'Tracy','Michael']
print(classmates)
print(classmates.__len__())
print(len(classmates))
print(classmates[0])
print(classmates[-1])

classmates.append('Adam')
print(classmates.pop())

## slice
l = range(100)
# 第一个是起始位子，第二个是长度
print(l[0:10])
#
print(l[:10])
print(l[-10:])   # 后10个
print(l[:10:2])  # 前十个，每间隔2个取一个，一共取出5个
print(l[::5])    # 每隔5个取出一个

# tuple 也可以做 slice 操作
print((0, 1, 2, 3, 4, 5)[:3])

print(classmates)
classmates[1] = 'Sarah'
print(classmates)

classmates.sort()
print(classmates)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s.__len__())
print(len(s[2]))
print(s[2][1])

## dict
d = {'Michael': 95, 'Fred': 75, 'Tracy': 85}
print('Michael =', d['Michael'])
d['Tracy'] = 86
print('Tracy =', d['Tracy'])
d['Adam'] = 67
print('Adam =', d['Adam'])

if 'Fred' in d:
    d.pop('Fred')
    print(d)
else:
    print('Fred is not in!')

## set
s = set([1, 2, 3])
print(s)

# set member will never duplicate
s = set([1, 1, 2, 2, 3, 3])
print(s)

s.remove(2)
print(s)

# tuple:
# 注意：tuple是一个实体，一旦形成不可改变。list 是多个实体的集合，每个成员都可以修改，两种有本质区别
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)

# 如果只有一个元素，那么"()"代表的是运算，而不是tuple，如果要表达tuple需要加上逗号","
print((1), (1,))

# 因此在打印一个元素的tuple的时候，也会自动加上逗号","
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
