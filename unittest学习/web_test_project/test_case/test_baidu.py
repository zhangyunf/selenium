#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

from selenium import webdriver
import unittest,time

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.baidu.com"


    def test_baidu(self):
        u'''百度测试用例'''
        self.driver.get(self.base_url + "/")
        self.driver.find_element_by_id("kw").clear()
        self.driver.find_element_by_id("kw").send_keys("unittest")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, u"unittest_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    print("进入")
    unittest.main()
