# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''
    获取所有的页面的链接
'''
import requests
import re
from bs4 import BeautifulSoup
from one_page_blog_link import OnePageBlogLink


class GetAllBlogPages:
    def __init__(self, url_str,url):
        self.url_str = url_str
        self.url=url

    # 获取最大的页码
    def get_max_page_num(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        page_str = soup.find_all('a', text='尾页')[0]['href']
        return int(re.findall(re.compile(r'.+?-(.+?).html'), page_str)[0])

    # 获取所有的页面的链接
    def get_all_pages(self):
        page_urls = []
        for page in range(1, self.get_max_page_num() + 1):
            page_url = self.url_str + str(page) + '.html'
            page_urls.append(page_url)
        return page_urls

# url = 'http://blog.ifeng.com/2675094-1.html'
# url_str = 'http://blog.ifeng.com/2675094-'
# page = OnePageBlogLink(url)
# page_num = int(page.get_page_contents()[2])
# all_pages = GetAllBlogPages(url_str,url)
# print(len(all_pages.get_all_pages()))
# print(all_pages.get_all_pages()[all_pages.get_max_page_num()-1]=='http://blog.ifeng.com/2675094-52.html')
# print(all_pages.get_max_page_num())
# print(all_pages.get_all_pages(url))
# print(all_pages.get_max_page_num())
# print(type(all_pages.get_max_page_num()))
