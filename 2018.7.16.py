# import sys
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
# f = fibonacci(20)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
# def hello() :
#    print("Hello World!")
# print(hello(1)
# !/usr/bin/python3

# # 定义函数
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
#
#
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")
# !/usr/bin/python3

# 可写函数说明
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
#
#
# # 调用printme函数
# printme()
# !/usr/bin/python3

# # 可写函数说明
# sum = lambda arg1, arg2: arg1 + arg2
#
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))
# !/usr/bin/python3
#
# num = 1
#
#
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)


# fun1()
# matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
# print(row[i] for row in matrix] for i in range(4)])if __name__ == '__main__':
#!/usr/bin/python3
# Filename: using_name.py

#     if __name__ == '__main__':
#         print('程序自身在运行')
#     else:
#         print('我来自另一模块')
# # import using_name
# def aa(a):
#     print(a)
#     aa=(22)

# 递归
# def aa(a):
#     print(a)
#     aa(22)
#
# aa(1)
# def jiafa(n):
#     if n == 1:
#         return 1
#     return n + jiafa(n - 1)
#
#
# print(jiafa(10))


#
# a=[2,5,3,8,6,1,9,0,7,4]
# n=len(a)
#
#
# def bj(i):
#     if a[i] > a[i + 1]:
#         b = a[i];
#         c = a[i + 1]
#         a[i + 1] = b
#         a[i] = c
#         bj(i + 1)
#     else:
#         i += 1
#         return a
# def dg(i):
#     while i<n:
#         bj(i)
#         dg(i+1)
#     else:
#         return a
# print(a)
# dg(0)
#
#
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
# # 注意前一行 'end' 的使用
#     print(repr(x*x*x).rjust(4))
# for x in range(1, 11):
#      print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
# print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
#!/usr/bin/python3
#!/usr/bin/python3
#
# # 打开一个文件
# f = open("/tmp/foo.txt", "w")
#
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
#
# # 关闭打开的文件
# f.close()
# while True :print('Hello world')
# 10 * (1/0)
# while True:
#         try:
#             x = int(input("Please enter a number: "))
#             break
#         except ValueError:
#             print("Oops!  That was no valid number.  Try again   ")






