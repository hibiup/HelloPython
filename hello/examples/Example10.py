#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

__author__ = 'Anonymous'

############################
# (object)，表示该类是从哪个类继承下来的。object类是所有类最终都会继承的类
class Student(object):
    # 构造函数。__init__方法的第一个参数永远是self。有了__init__方法，在创建实例的时候，就不能传入空的参数了，
    # 必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
    def __init__(self, name, score):
        self.__name = name                # 外部无法直接访问 "__" 开头的变量
        self.__score = score

    # 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    # getter & setter
    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')   # raise 抛出异常

    # @property 是一个decorator ，修饰了 weight 的 setter方法
    @property
    def weight(self):
        return self._weight

    # 修饰 weight 的 setter方法。会由 @property 动态创建，也可以不定义
    @weight.setter
    def weight(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._weight = value

    # print 的时候被调用
    def __str__(self):
        return 'Student object (name: %s)' % self.__name

    # __repr__ report 的简称，用于debug，以下让它和 __str__输出一样
    __repr__ = __str__

    # 缺省调用
    def __call__(self):
        return 'Student() is called'


############################
# 以构造方式生成实例使，不使用 new
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
print(bart)
print(bart())
bart.print_score()
lisa.print_score()

# python是动态语言，可以随时新增属性
bart.age = 90
print(bart.age)
print(hasattr(bart,'age'))

del bart.age
print(hasattr(bart,'age'))

# 还可以新增方法
from types import MethodType
def set_age(self, age): # 定义一个函数作为实例方法
     self.age = age
bart.set_age = MethodType(set_age, bart)
bart.set_age(25)
print(bart.age)

print(hasattr(bart,'set_age'))
del(bart.set_age)
print(hasattr(bart,'set_age'))

# 为了给所有实例都绑定方法，可以给class绑定方法
Student.set_age = set_age
bart.set_age(100)
print(bart.age)

############################
# type:
# 而h是一个实例，它的类型就是class
print(type(bart))
# Hello是一个class，它的类型就是type
print(type(Student))
print(type(bart.print_score))

import types
print(type(bart.print_score) == types.MethodType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

print(isinstance(bart, Student))
print(isinstance(b'a', bytes))

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir('ABC'))
print(dir(bart))
print(dir(lambda x: x))
print(dir(x for x in range(10)))

# 用 type 动态创建一个类
def fn(self, name='world'):
    print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
print(type(Hello))
h = Hello()
print(getattr(h,'hello'))
h.hello()

################################
# metaclass: 元类
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。先定义metaclass，就可以创建类，最后创建实例。换句话说，你可以把类看成是metaclass创建出来的“实例”。
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass

# 这个metaclass可以给我们自定义的MyList增加一个add方法
class ListMetaclass(type):         # metaclass是类的模板，所以必须从`type`类型派生：
    # __new__()方法接收到的参数依次是：
    #   当前准备创建的类的对象；
    #   类的名字；
    #   类继承的父类集合；
    #   类的方法集合。
    def __new__(cls, name, bases, attrs):
        # 实例包含一个名为 add 的方法
        attrs['add'] = lambda self, value: self.append(value)
        # 用 type 创建新的类
        return type.__new__(cls, name, bases, attrs)

# 指定使用 ListMetaclass 来定制类.它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
print(isinstance(L, list))
print(isinstance(L, MyList))
L.add(1)
print(L)