#coding=UTF-8

'''
练习【二】：启动、关闭浏览器
1.启动浏览器
2.等待3s
3.关闭浏览器
'''
from selenium import webdriver
from time import sleep

#IE浏览器
dr=webdriver.Ie()

sleep(3)

#退出浏览器close()方法
#close方法仅关闭当前浏览器窗口
#dr.close()

#quit方法不仅关闭浏览器窗口，还会彻底的退出webdriver
#释放driver server之间的连接。
#quit比close更好的释放资源

dr.quit()

#Chrome浏览器
dr=webdriver.Chrome()

sleep(3)

dr.quit()

#Firefox浏览器
dr=webdriver.Firefox()

sleep(3)

dr.quit()

