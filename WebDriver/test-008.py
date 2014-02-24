#coding= utf-8
'''
【练习八】：定位一组对象
'''

from selenium import webdriver
from time import sleep
import os

filepath="file:///"+ os.path.abspath("checkbox.html")
dr = webdriver.Chrome()
dr.get(filepath)

# 找到所有的checkbox 并全部勾上（通过css）
checkboxes=dr.find_elements_by_css_selector('input[type=checkbox]')

for checkbox in checkboxes:
	checkbox.click()

sleep(4)

#去掉最后一个checkbox的勾
dr.find_elements_by_css_selector('input[type=checkbox]').pop().click()

sleep(2)

#找到所有radio并勾上
inputs= dr.find_elements_by_tag_name('input')

for input in inputs:
	if input.get_attribute('type') == 'radio' :
   		input.click()

#打印所有input控件个数
print "所有input的个数为%s" %(len(dr.find_elements_by_tag_name('input')))
#打印checkbox个数
print "共有%s个checkbox"%(len(dr.find_elements_by_css_selector('input[type=checkbox]')))
#打印radio个数
print "共有%s个radio"%(len(dr.find_elements_by_css_selector('input[type=radio]')))

sleep(2)

dr.quit()