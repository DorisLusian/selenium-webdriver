#coding= utf-8

'''
【练习二十】：form的操作
1. 使用send_keys方法往多行文本框和单行文本框赋值；
2. 使用click方法选择checkbox
3. 使用click方法选择radio
4. 使用click方法点击button
5. 使用click方法选择option，从而达到选中select下拉框中某个具体菜单项的效果

'''

from selenium import webdriver
from time import sleep
import os

dr = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('form.html')
dr.get(file_path)

# 选中checkbox
dr.find_element_by_css_selector('input[type=checkbox]').click()
sleep(1)

# 选中radio
dr.find_element_by_css_selector('input[type=radio]').click()
sleep(1)

# 选择下拉菜单中的最后一项
dr.find_element_by_tag_name('select').find_elements_by_tag_name('option')[-1].click()
sleep(1)

# 点击提交按钮
dr.find_element_by_css_selector('input[type=submit]').click()
sleep(10)

alert = dr.switch_to_alert()
print alert.text
alert.accept()

dr.quit()