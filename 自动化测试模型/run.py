#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest
from selenium.webdriver.common.by import By
import csv
url = r"https://pan.baidu.com/"

class sign_up_page(object):
    def __init__(self, driver):
        self.driver = driver
    def sign_up_btn(self):
        try:
            element = WebDriverWait(self.driver, 5, 0.5).until(EC.visibility_of_element_located((By.ID, r"TANGRAM__PSP_4__footerULoginBtn")))
            element.click()
            self.driver.implicitly_wait(10)
        except Exception as e:
            print("error:", e)



class MyTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(url)
        self.browser.maximize_window()
        time.sleep(2)

    def testOne(self):
       signPage = sign_up_page(self.browser)
       signPage.sign_up_btn()
       current_title = self.browser.title
       self.assertEqual("百度网盘，让美好永远陪伴", current_title)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()

