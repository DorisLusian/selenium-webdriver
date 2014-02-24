#coding=UTF-8
'''
【练习一】
 1.打开谷歌浏览器
 2.输入百度网址
 3.点击贴吧链接
 4.等待5s
 5.退出浏览器
'''

from selenium import webdriver
from time import sleep

#打开谷歌浏览器
dr = webdriver.Chrome() 
#dr = webdriver.Ie()
#dr = webdriver.Firefox()
url='http://www.baidu.com'
dr.get(url)

dr.find_element_by_link_text(u"贴 吧").click()

sleep(5)

dr.quit()