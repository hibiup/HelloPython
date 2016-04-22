#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 文件就是模块名，比如这个模块的名字就叫 Example9。下面这一行是模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
' a test module '

# 作者
__author__ = 'Someone'

#  以上是Python模块的标准文件模板
##########################################
# 下面开始就是真正的代码部分。

import sys

# _ 或 __ 开头的函数是私有函数
def _private_1(name):
    return 'Hello, %s' % name

def greeting():
    args = sys.argv     # sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print(_private_1(args[1]))    # 引用私有函数
    else:
        print('Too many arguments!')

# 如果入口是 main，也就是直接执行，比如命令行: python Example9.py。则执行。而如果在其他地方导入该模块，if 判断将失败
if __name__=='__main__':
    greeting()
# 其他地方引用该模块的方法是直接调用 Example9.greeting()

#####################################################################
# 在Python中，安装第三方模块可以通过包管理工具pip完成。例如：
# > pip install Pillow
# > vi a.py
# ...
# from PIL import Image
# im = Image.open('test.png')
# ...
#
# 其他常用的第三方库还有MySQL的驱动：mysql-connector-python，用于科学计算的NumPy库：numpy，用于生成文本的模板工具Jinja2
#
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错。
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中
print(sys.path)