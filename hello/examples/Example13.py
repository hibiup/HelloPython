#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

__author__ = 'Anonymous'

import logging

logging.basicConfig(level=logging.INFO)


class Err(object):
    def foo(s):
        n = int(s)

        try:
            # 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代. 如果断言失败，assert语句本身就会抛出AssertionError
            assert n != 0, 'n is zero!'
        except AssertionError as e:
            logging.info('n = %d' % n)
            raise e

        return 10 / n

try:
    e = Err()
    e.foo('0')
except Exception as e:
    logging.info(e)


#########################################
# 单元测试
#
# 测试目标
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


# 编写单元测试
import unittest


class TestDict(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    # 以test开头的方法就是测试方法
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        # 指明期待抛出的 Error 类型
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

# 运行单元测试
if __name__ == '__main__':
    unittest.main()
