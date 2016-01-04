# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''
    保存所有的图片
'''
import os
from get_all_blog_pages import GetAllBlogPages
from one_page_blog_link import OnePageBlogLink
from save_photos import SavePhotos as sp
from get_blog_photo_link import GetBlogPhotoLink as gbpl
from dir import Dir


class SaveAllPhotos:
    def __init__(self, path, url):
        self.path = path
        self.url = url

    # 保存所有页面的图片
    def save_all_photos(self):
        gabp = GetAllBlogPages(self.url)

        for page_url in gabp.get_all_pages():
            opbl = OnePageBlogLink(page_url)
            blog_page_urls = opbl.get_blog_page_urls()
            # 保存一个页面上的所有blog链接到的图片
            for blog_page_url_num in range(0, len(blog_page_urls)):
                Dir().ch_dir(self.path)
                Dir().make_dir(opbl.get_blog_page_contents()[1][blog_page_url_num][0])
                new_path = os.path.join(self.path, opbl.get_blog_page_contents()[1][blog_page_url_num][0])
                Dir().ch_dir(new_path)
                photo_urls = gbpl(blog_page_urls[blog_page_url_num]).get_photo_urls()
                sp().save_one_page_photos(photo_urls)
