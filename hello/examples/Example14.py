#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test class example '

# 把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling. 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。反过来，
# 把变量内容从序列化的对象重新读到内存里称之为反序列化，即 unpickling。

import pickle

d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d))

f = open('dict.dump', 'wb')
pickle.dump(d, f)
f.close()

f = open('dict.dump', 'rb')
d = pickle.load(f)
f.close()
print(d)
