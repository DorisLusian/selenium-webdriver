#coding= UTF-8
'''
【练习三】：最大化浏览器
1.启动浏览器
2.最大化浏览器
3.等待3s
4.退出浏览器
'''

from selenium import webdriver
import time

dr = webdriver.Chrome()

time.sleep(3)

#print'最大化浏览器'

dr.maximize_window()

time.sleep(3)

#print'关闭浏览器'

dr.quit()

