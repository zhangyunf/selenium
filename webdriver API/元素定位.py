#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://pan.baidu.com/")

try:
    time.sleep(2)
    driver.find_element(By.ID, 'TANGRAM__PSP_4__footerULoginBtn').click()

    driver.find_element(By.NAME, value="userName").send_keys("17694839025")
    driver.find_element(By.XPATH, "//*[@type='password']").send_keys("feina1799")
    driver.find_element(By.CSS_SELECTOR, ".pass-text-input pass-text-input-password").click()
except Exception:
    print("出错了")
    # driver.quit()
finally:
    pass
    # driver.quit()

