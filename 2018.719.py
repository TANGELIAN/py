# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()
# !/usr/bin/python3

# class MyClass:
# #     """一个简单的类实例"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
#
#
# # 实例化类
# x = MyClass()
#
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f())
#!/usr/bin/python3
import math   # 导入 math 模块
a=math.modf(100.12)
print (      a)