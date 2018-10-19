#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
#计算器类

class Count:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    #计算加法
    def add(self):
        return self.a + self.b

    #扩充减法功能
    def subt(self):
        return self.a - self.b
