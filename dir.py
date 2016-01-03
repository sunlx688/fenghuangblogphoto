# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''
    创建目录和改变目录路径
'''
import os


class Dir:
    # 创建目录
    def make_dir(self, dir_name):
        is_exists = os.path.exists(dir_name)
        if not is_exists:
            print('创建名为', dir_name, '的目录')
            os.mkdir(dir_name)
        else:
            print('目录', dir_name, '已存在！')

    # 修改目录路径
    def ch_dir(self, path):
        print('改变当前路径为', path)
        os.chdir(path)
