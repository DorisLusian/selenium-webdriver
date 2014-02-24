#coding= utf-8

'''
【练习十】：操作对象
1.click 点击对象
2.send_keys 在对象上模拟按键输入
3.clear 清除对象的内容
'''
from selenium import webdriver
from time import sleep

dr= webdriver.Chrome()
url= "http://www.baidu.com"
dr.get(url)

# click
dr.find_element_by_link_text(u"贴 吧").click()

sleep(3)

dr.back()

sleep(3)

#send_keys、clear()
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()

sleep(3)

dr.back()

sleep(3)
dr.find_element_by_id("kw").send_keys("python")
sleep(2)
dr.find_element_by_id("kw").clear()

sleep(2)
dr.quit()