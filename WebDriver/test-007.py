#coding= utf-8
'''
【练习七】：简单的定位对象
'''

from selenium import webdriver
from time import sleep
import os


dr =webdriver.Chrome()
file_path ='file:///' + os.path.abspath('form.html')
print file_path

dr.get(file_path)

sleep(4)

# by id
dr.find_element_by_id('inputEmail').click()

# by name
dr.find_element_by_name('password').click()

# by tagname
print dr.find_element_by_tag_name('form').get_attribute('class')

# by class_name
e = dr.find_element_by_class_name('controls')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',e)

sleep(2)

# by link text
link =dr.find_element_by_link_text('register')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)

sleep(2)

# by partial link text
link = dr.find_element_by_partial_link_text('reg')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',link)

sleep(2)

# by css selector
div = dr.find_element_by_css_selector('.controls')
dr.execute_script('$(arguments[0]).fadeOut().fadeIn()',div)

sleep(2)

# by xpath
dr.find_element_by_xpath('/html/body/form/div[3]/div/label/input').click()

sleep(3)

dr.quit()

