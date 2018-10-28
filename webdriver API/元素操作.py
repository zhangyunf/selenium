#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://pan.baidu.com/")
time.sleep(2)
element = driver.find_element(By.ID, 'TANGRAM__PSP_4__footerULoginBtn')
#查看元素是否可见
print(element.is_displayed())
#返回元素的文本
print(element.text)
#返回元素尺寸
print(element.size)
#获取属性值
print(element.get_attribute("id"))
driver.quit()