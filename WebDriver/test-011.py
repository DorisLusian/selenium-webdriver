#coding= utf-8

'''
【练习十一】：send keys模拟按键输入
1.从A文本框中拷贝内容
2.粘贴到B文本框中
3.在A框中输入
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('send_keys.html')

dr.get(file_path)

# copy content of A
dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'a'))
dr.find_element_by_id('A').send_keys((Keys.CONTROL, 'x'))
sleep(1)

# paste to B
dr.find_element_by_id('B').send_keys((Keys.CONTROL, 'v'))
sleep(1)

# # send keys to A
dr.find_element_by_id('A').send_keys('watir', '-', 'webdriver', Keys.SPACE, 'is', Keys.SPACE, 'better')
sleep(2)

dr.quit()
