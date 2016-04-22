# Example7.py
# -*- coding: utf-8 -*-

################################
## log() 增强now()函数的功能，在函数调用前后自动打印日志，类似 AOP。这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 使用 decorator
# 当函数 now 被调用的时候，首先会调用它的装饰器 log，并将自己做为参数传给它。于是 log 就被执行了，并返回 wrapper 代替了 now
@log
def now():
    print('2015-3-25')

now()
# 这里执行的并不是真的 now ，而是 log返回的 wrapper。wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。
print(now.__name__)

## 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数。
import functools
def log(text):
    def decorator(func):
        # 返回的那个 now 函数实际上是'wrapper',需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
        # Python内置的functools.wraps就是干这个事的
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

# 首先执行log('execute')，返回的是decorator函数，再调用返回的函数，返回wrapper函数。
@log('execute')
def now():
    print('2015-3-25')

now()
print(now.__name__)