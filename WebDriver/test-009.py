#coding= utf-8
'''
【练习九】：层级定位
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


dr= webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('level_locate.html')
dr.get(file_path)

#点击Link1链接(弹出下拉列表)
dr.find_element_by_link_text('Link1').click()

#找到id为dropdown1的父元素
WebDriverWait(dr,10).until(lambda the_driver: the_driver.find_element_by_id('dropdown1').is_displayed())

#在父元素下找到link为Action的子元素
menu= dr.find_element_by_id('dropdown1').find_element_by_link_text('Action')

#鼠标移动到子元素上
webdriver.ActionChains(dr).move_to_element(menu).perform()

sleep(3)

dr.quit()



