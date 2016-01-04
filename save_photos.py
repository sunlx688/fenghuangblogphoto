# -*- coding:utf-8 -*-
__author__ = 'SUN'
import os
import requests
from time import sleep

'''
    保存图片
'''


class SavePhotos:
    def __init__(self):
        pass

    # 保存一张图片
    def save_one_photo(self, file_name, img_url):
        buff = requests.get(img_url).content
        fp = open(file_name, 'wb')
        fp.write(buff)
        fp.close()

    # 保存一页上的图片
    def save_one_page_photos(self, photo_urls):
        x = 1
        print('本页共有', len(photo_urls), '张图片')
        for photo_url in photo_urls:
            if os.path.exists('%s.jpg' %x):
                pass
            else:
                print('保存本页中的第', x, '张图片')
                self.save_one_photo('%s.jpg' % x, photo_url)
                x += 1
                sleep(0.1)
        print('本页的图片已保存完成！')


