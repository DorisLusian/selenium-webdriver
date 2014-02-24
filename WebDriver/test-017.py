#coding= utf-8

'''
【练习十七】：获取测试对象的属性及内容

'''
from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('attribute.html')

dr.get(file_path)

link = dr.find_element_by_id('tooltip')

sleep(1)
# 获得tooltip的内容
print link.get_attribute('data-original-title')

# 获取该链接的text
print link.text

dr.quit()