# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''
    获取一页中的所有图片链接
'''
import os
import re
import requests
from bs4 import BeautifulSoup
from time import sleep


class GetBlogPhotoLink:
    def __init__(self, url):
        self.url = url

    # 获取图片链接的信息
    def get_msgs(self):
        res = requests.get(self.url)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text, 'html.parser')
        msgs = soup.find_all('img', attrs={"style": "float:none;"})
        return msgs

    # 获取图片的链接
    def get_photo_urls(self):
        photo_urls = []
        msgs = self.get_msgs()
        for msg in msgs:
            photo_url = msg['src']
            photo_urls.append(photo_url)
        return photo_urls


# url = 'http://blog.ifeng.com/article/42168009.html'
#
# photo = GetBlogPhotoLink(url)
# print(photo.get_msgs())
# print(type(photo.get_photo_urls()))
# print(photo.get_photo_urls()[0])
# print(type(photo.get_photo_urls()[0]))