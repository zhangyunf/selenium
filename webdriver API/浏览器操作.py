#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
#刷新
driver.refresh()
#返回当前浏览器的url
print(driver.current_url)
#返回当前页面title
current_title = driver.title
print("title:", current_title)
#返回当前窗口的句柄，多窗口切换时会用到
handler = driver.current_window_handle
#返回所有的句柄
all_handler = driver.window_handles
print("handler %s\n all_handler %s" % (handler, all_handler))



driver.maximize_window()
print(driver.get_window_size(handler))

driver.quit()


