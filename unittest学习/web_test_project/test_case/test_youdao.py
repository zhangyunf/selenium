#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from selenium import webdriver
import unittest, time


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.youdao.com"

    def test_baidu(self):
        self.driver.get(self.base_url + "/")
        self.driver.find_element_by_id("query").clear()
        self.driver.find_element_by_id("query").send_keys("webdriver")
        self.driver.find_element_by_id("qb").click()
        time.sleep(2)
        title = self.driver.title
        self.assertEqual(title, u"webdriver - 有道搜索")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()