#-*- coding:utf-8 -*-
#!Author:YunFei Zhang

from count import Count
import unittest

class test(unittest.TestCase):
    #进行测试前的初始化
    def setUp(self):
        print("开始测试")
    def test1(self):
        count = Count(2, 3)
        self.add = count.add()
        self.assertEqual(self.add, 5)
    def tearDown(self):
        print("测试完成")

'''
if __name__ == "__main__":
    unittest.main()
'''

if __name__ == "__main__":
    #构造测试集
    suite = unittest.TestSuite()
    suite.addTests(test("test1"))

    #执行
    runner = unittest.TextTestRunner()
    runner.run(suite)
