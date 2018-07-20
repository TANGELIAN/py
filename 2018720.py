# import re
# print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# !/usr/bin/python3
# import re
#
# line = "Cats are smarter than dogs"
#
# matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
#
# if matchObj:
#     print("matchObj.group() : ", matchObj.group())
#     print("matchObj.group(1) : ", matchObj.group(1))
#     print("matchObj.group(2) : ", matchObj.group(2))
# else:
#     print("No match!!")
#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# for i in range(1,5):
#     for l in range(1,5):
#         for v in range(1,5):
#             if i!=l and l!=v and v!=i:
#                 print (i,l,v)

# def jiangjin(i):
#     if i<=100000:
#         return i*0.1
#     elif 100000<=i<200000:
#         return i*0.1+(i-10000)*0.075
#     elif 200000<=i<400000:
#         return i*0.1+10000*0.075+(i-200000)*0.05
#     elif 400000<=i<600000:
#         return i*0.1+10000*0.075+200000*0.005+(i-400000)*0.03
#     elif 600000<=i<1000000:
#         return i*0.1+10000*0.075+200000*0.005+200000*0.003+(i-600000)*0.015
#     elif 1000000<=i:
#         return i*0.1+10000*0.075+200000*0.005+200000*0.003+400000*0.015+(i-1000000)*0.01
# a=int(input('本月利润：'))
# print('本月奖金：',jiangjin(a))
#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math
def qwe(t):
    a=math.modf(t)
    c=list(a)
    b=c[0]
    return b
m=-100
x = math.sqrt(m + 100)
y = math.sqrt(m + 268)
while qwe(x)!=0 and qwe(y)!=0:
    m+=1
else:
    print(m)


















