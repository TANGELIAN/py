# flag=True
# if flag:
#     print('你好')
# else:
#     print('去死 ')
# print ("Hello, Python!");
#! /usr/bin/env python3
# def a():
#     '''这是文档字符串'''
#     pass
# print(a.__doc__)
# a=1;b=1;c=3
# d=a+b+c
# print(d)
# !/usr/bin/python3
#
# a = 21
# b = 10
# c = 0
#
# c = a + b
# print("1 - c 的值为：", c)
#
# c = a - b
# print("2 - c 的值为：", c)
#
# c = a * b
# print("3 - c 的值为：", c)
#
# c = a / b
# print("4 - c 的值为：", c)
#
# c = a % b
# print("5 - c 的值为：", c)
# a=20;b=10
# if (a and b):
#     print("1 - 变量 a 和 b 都为 true")
# else:
#     print("1 - 变量 a 和 b 有一个不为 true")
#
# if (a or b):
#     print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#     print("2 - 变量 a 和 b 都不为 true")
# !/usr/bin/python3
#
# var1 = 'Hello World!'
# var2 = "Runoob"
#
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])
# !/usr/bin/python3
#
# var1 = 'Hello World!'
#
# print("已更新字符串 : ", var1[:6] + 'Runoob!')
# a='asdfg'
# 'f' in a
# !/usr/bin/python3

# para_str = """这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB ( \t )。
# 也可以使用换行符 [ \n ]。
# """
# print(para_str)
# a=[1,2,4]
# print(a)
num=[2,3,4,6,1]
m=0
while m<len(num):
        if num[m]<num[m+1]:
            num[m+1]=num[m]
        m+=1
        print(m)