#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
time.sleep(2)
browser.maximize_window()
element = browser.find_element_by_id("kw")
element.send_keys("seleniumm")
time.sleep(5)
#删除多余的m
element.send_keys(Keys.BACK_SPACE)
time.sleep(5)
#回车
element.send_keys(Keys.ENTER)
browser.quit()
