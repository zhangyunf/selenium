#-*- coding:utf-8 -*-
#!Author:YunFei Zhang
def foo():
    return [lambda x: i+x for i in range(4)]
print(foo())
a = foo()
for x in a:
    print(x)
print([x(3) for x in foo()])