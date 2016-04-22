#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' start web server '

##############################################
# 这个应用会启动 python 自带的一个缺省的 wsgi(web) 服务。然后获引入webservice.py 中的方法提供服务。但是这显然太原始了。
# flaskservie.py 演示了另一种通过 Flask 框架提供 rest 服务的例子。Flask 的安装参考相关文档


# server.py
# 从wsgiref模块导入:
from wsgiref.simple_server import make_server
# 导入我们自己编写的 webservice 函数:
from hello.web.wsgi.webservice import home


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
