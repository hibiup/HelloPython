#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

__author__ = 'Anonymous'

#####################################
# 下面这个例子假设了一个 Rest 调用, 我们需要动态地适应 URI 的路径(path)
class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __str__(self):
        return self._path

    __repr__ = __str__

    # 返回 URI
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

print(Chain().status.user.timeline.list)
# 用decorator 实现以下功能
#print(Chain().status.users('michael').repos)