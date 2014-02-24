#coding= utf-8

'''
【练习二十五】：action

'''
from selenium.webdriver.common.action_chains import ActionChains

element = wd.find_element_by_link_text('xxxxx')
hov = ActionChains(wd).move_to_element(element)
hov.perform()