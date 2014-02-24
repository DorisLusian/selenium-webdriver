# coding=utf-8

'''
【练习六】:页面的前进与后退
1. 打开浏览器
2. 输入第一个网址，打印当前网址
3. 等待3s
4. 输入第二个网址，打印当前网址
4. 执行后退操作，打印后退后的网址
5. 执行前进操作，打印前进后的网址
'''

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
firsturl = 'http://www.baidu.com/'
dr.get(firsturl)

sleep(3)

secondurl = 'http://joyinwise.com'
dr.get(secondurl)

dr.back()
print "URL of current page is %s"%(dr.current_url)

dr.forward()
print "URL of current page is %s"%(dr.current_url)

sleep(3)

dr.quit()
