# -*- coding:utf-8 -*-
__author__ = 'SUN'
'''
    获取一个页面中所有的blog页面链接
'''

import requests
import re
from bs4 import BeautifulSoup


class OnePageBlogLink:
    # 初始化对象
    def __init__(self, url):
        self.url = url

    # 获取页面的框架
    def get_soup(self):
        response = requests.get(self.url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    # 获取页面链接的框架
    def get_msgs(self):
        soup = self.get_soup()
        msgs = soup.find_all('h3')
        page_num_str = soup.find_all('span', attrs={"class": "current"})
        return msgs, page_num_str

    # 获取blog页面的链接和目录名
    def get_blog_page_contents(self):
        msgs = self.get_msgs()[0]
        page_num_str = self.get_msgs()[1]
        page_htmls = []
        page_titles = []
        for msg in msgs:
            msg = str(msg)
            page_htmls.append(re.findall(re.compile(r'.+?href="(.+?)".+?'), msg))
            page_titles.append(re.findall(re.compile(r'.+?title="(.+?)".+?'), msg))
        page_num = re.findall(re.compile(r'<span class="current">(.+?)</span>'), str(page_num_str))[0]
        return page_htmls, page_titles, page_num

    # 获取一个页面中所有的blog页面链接
    def get_blog_page_urls(self):
        page_urls = []
        url_str = 'http://blog.ifeng.com'
        page_htmls = self.get_blog_page_contents()[0]
        for page_html in page_htmls:
            page_url = url_str + page_html[0]
            page_urls.append(page_url)
        return page_urls

# url = 'http://blog.ifeng.com/2675094-53.html'
# link = OnePageBlogLink(url)
# # print(link.get_msgs())
# print(len(link.get_blog_page_urls()))