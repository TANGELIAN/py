# favorite_places={'小明':{'place':['上海','北京']},'小明':{'place':['深圳','北京']}}
# for i in range(1,4):
# #     print(i)
# one={'name:小黄','tepy:金毛','master:小明'}
# two={'name:小红','tepy:泰迪','master:小强'}
# there={'name:小黑','tepy:大丹','master:小梁'}
# pets=[one,two,there]
# for i in pets:
#     print('%s的种类是%s，它的主人是%s:'%(i))
# a=[1,2,3,4]
# print(id(a))
# a=[2,3,4,5]
# b=a
# print(id(a))
# print(id(b))
# import copy
# # a=[1,2,3]
# # b=copy.copy(a)
# # print(id(a))
#
# print(id(b))
# a=[1,2,3]
# b=a
# print(id(a))
# print(id(b))
# !/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b
# a=[1,2,3]
# b=[1,2,3]
# print(id(a))
# print(id(b))
#Fibonacci series: 斐波纳契数列
#两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b
# x = int(input("Please enter first value1: "))
# y = int(input("Please enter second value2: "))
# z = int(input("Please enter second value3: "))
# if (x == y==z):
#     print("三数相同！")
# elif (x > y):
#     if (z>x):
#         print("最大数为：",z)
#     else:
#         print("最大数为：", x)
# elif (y > x):
#     if (z>y):
#         print("最大数为：",z)
#     else:
#         print("最大数为：", y)
# strings = ['import','is','with','if','file','exception']
# D = {key: val for val,key in enumerate(strings)}
# print(dict(D))
#coding:utf-8
# rows = int(raw_input('输入列数： '))
# i = j = k = 1 #声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
# #等腰直角三角形1
# print("等腰直角三角形1")
# for i in range(0, rows):
#     for k in range(0, rows - i):
#         print(" * "), #注意这里的","，一定不能省略，可以起到不换行的作用
#         k += 1
#     i += 1
# #     print ("\n")


# list1=[1,2,3,4]
# a=iter(list1)
# for b in a:
#     print(b)
# !/usr/bin/python3

import sys  # 引入 sys 模块

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象

# while True:
#     try:
#         print(next(it),end='')
#     except StopIteration:
#         sys.exit()
# !/usr/bin/python3

# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)# f 是一个迭代器，由生成器返回生成
# !/usr/bin/python
# -*- coding: UTF-8 -*-

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用 yield
        # print b
        a, b = b, a + b
        n = n + 1

# for n in fab(5):
#     print(n)

#
# it = fab(5)

# h = int(input('输入高度'))
# c = 0
# n = h
# t = int(input('想要多少次落地'))
# while c<t:
#     n += h
#     h/=2
#     print(n)
#     c+=1
# print('第10此返回%s米'%h)
# print('共经过%s米'%n)
l=int(input('绳子的长度;'))
t=0
a=int(input('绳子最短:'))
while l>=a :
    t+=1
    l/=2

print('天数：%s'%t)






