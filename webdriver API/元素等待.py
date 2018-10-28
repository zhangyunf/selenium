#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait#显示等待引入
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
import time
driver = webdriver.Chrome()
driver.get("https://pan.baidu.com/")
print(EC.url_to_be("https://pan.baidu.com/"))
#隐式等待
driver.implicitly_wait(2)
#显式等待判断元素是否存在并且可见
element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'TANGRAM__PSP_4__footerULoginBtn')))
AC(driver).click(element).perform()
driver.get_screenshot_as_file(r"D:\截图\1.png")
#强制等待
time.sleep(5)
driver.quit()
