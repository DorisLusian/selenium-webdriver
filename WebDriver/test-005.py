# -*- coding: utf-8 -*-
'''
【练习五】：打印当期页面的title和url
1.打开谷歌浏览器
2.访问链接
3.打印当前页面的title
4.打印当前页面的url
'''

from selenium import webdriver
from time import sleep
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


dr = webdriver.Chrome()
url = "http://www.baidu.com/"
dr.get(url)

print "Title of current page is %s" %(dr.title)
print "URL of current page is %s" %(dr.current_url)

sleep(3)

dr.quit()

