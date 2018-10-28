#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
import time
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
time.sleep(2)
browser.maximize_window()
# element = browser.find_element_by_id("kw")
# #右击
# AC(browser).context_click(element).perform()
# time.sleep(10)
element1 = browser.find_element_by_xpath('//*[@id="u1"]/a[8]')
#悬停
AC(browser).move_to_element(element1).perform()
time.sleep(10)

browser.quit()