# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''
    执行程序
'''

from save_all_photos import SaveAllPhotos as sap

url = 'http://blog.ifeng.com/2675094-1.html'
# url_str = 'http://blog.ifeng.com/2675094-'
path = 'G:\Code\img\原生泰\\blogpic'


def run():
    sap(path, url).save_all_photos()


# 运行函数
run()
