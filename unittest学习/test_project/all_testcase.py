#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
import unittest
from test_project import testadd, testsub

#构造测试集
'''
suite = unittest.TestSuite()
suite.addTest(testadd.test("test1"))
suite.addTest(testadd.test("test_add1"))
suite.addTest(testadd.test("test_add2"))

suite.addTest(testsub.TestSubt("test_subt"))
suite.addTest(testsub.TestSubt("test_subt1"))
'''

#使用discover方法
def creatSuite():
    testSuite = unittest.TestSuite()
    #定义测试文件查找目录
    test_dir = r"D:\selenium\unittest学习\test_project"
    #定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py", top_level_dir=None)

    #discover方法筛选出来用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testSuite.addTest(test_case)
    return testSuite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = creatSuite()
    runner.run(suite)