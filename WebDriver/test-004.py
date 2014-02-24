#coding= UTF-8
'''
【练习四】：定制浏览器大小
1.启动谷歌浏览器
2.将浏览器设置成移动端大小
3.访问移动站点
4.等待3s
5.关闭浏览器
'''

from selenium import webdriver
from time import sleep

dr = webdriver.Chrome()
dr.set_window_size(240,320)
dr.get('http://www.3g.qq.com/')

sleep(3)

dr.quit()