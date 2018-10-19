#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
from count import Count
import unittest

class TestSubt(unittest.TestCase):
    def setUp(self):
        print("测试减法")

    #整数相减
    def test_subt(self):
        sub = Count(10, 5)
        subt = sub.subt()
        self.assertEqual(subt, 5)
    #小数相减
    def test_subt1(self):
        sub = Count(10.1, 5.1)
        subt = sub.subt()
        self.assertEqual(subt, 5)

    def tearDown(self):
        print("测试减法结束")
if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestSubt("test_subt"))
    suite.addTest(TestSubt("test_subt1"))

    #执行
    runner = unittest.TextTestRunner()
    runner.run(suite)