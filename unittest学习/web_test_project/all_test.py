#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

import unittest
import HTMLTestRunner
from web_test_project.send_mail import send_mail
def creatSuite():
    suite = unittest.TestSuite()
    test_dir = r"D:\selenium\unittest学习\web_test_project\test_case"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py", top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            suite.addTest(test_case)
    return suite
if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = creatSuite()
    filename = r"D:\selenium\unittest学习\web_test_project\report\result.html"
    with open(filename, "wb") as fp:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u"test result",
                                               description=u"测试报告")
        runner.run(suite)




