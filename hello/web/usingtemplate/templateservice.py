#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' flash web services module '


#########################################################
# 这个例子中 web service 读取 jinja2 模版。jinja2 模版的安装命令是：
# (PROJECT_NAME) $ pip install jinja2
# jinja2 模版默认存放在 templates 目录下
#

from flask import Flask, request, render_template
import logging

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)


# 从请求URI中获得 home 的参数 "name"
@app.route('/<name>', methods=['GET', 'POST'])
def home(name):
    # 读取 jinja2 模版
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()  # Flask自带的Server在端口5000上监听
