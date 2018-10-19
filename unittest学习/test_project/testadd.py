#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from count import Count
import unittest

class test(unittest.TestCase):
    #进行测试前的初始化
    def setUp(self):
        print("开始测试")
    #整数相加
    def test1(self):
        count = Count(2, 3)
        self.add = count.add()
        self.assertEqual(self.add, 5)
    #测试小数相加
    def test_add1(self):
        count = Count(1.2, 2.3)
        add = count.add()
        self.assertEqual(add, 3.5)
    #测试字符串相加
    def test_add2(self):
        count = Count("hello", " world")
        add = count.add()
        self.assertEqual(add, "hello world")
    def tearDown(self):
        print("测试完成")

if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTests(tests=["test1", "test_add1", "test_add2"])

    #执行
    runner = unittest.TextTestRunner()
    runner.run(suite)