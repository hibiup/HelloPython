#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' start web server '

# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的 webservice 函数:
from hello.web.webservice import home


class Server():
    def __call__(self, *args, **kwargs):
        global services

        # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
        httpd = make_server('', 8000, home)
        print('Serving HTTP on port 8000...')
        # 开始监听HTTP请求:
        httpd.serve_forever()


server = Server()
server()
