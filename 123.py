# list=[1,2,3,4,'a','b']
# print(list[4])
# list.remove(3)
# print(list)
# myList = []
# for i in range(5)
# num = input()
# myList.append(num)
# a=range(1,5)
# print(a)
# a=int(print('数字A:'))
# b=int(print('数字B:'))
# c=a+b
# print(c)
# a=int(input('第一个数字A:'))
# b=int(input('第二个数字B:'))
# c=a+b
# print(c)
# a=int(input('数字A:'))
# b=int(input('数字B:'))
# c=a+b
# print(c)
#左上三角格式输出九九乘法表
# for i in range(1,10):
#     for j in range(i,10):
#         print("%d*%d=%2d" % (i,j,i*j),end=" ")
#     print("")

# for i in range(1,10):
#     for j in range(1,10):
#         print("%d*%d=%2d" % (i,j,i*j),end=" ")
#     print("")
# a,b,c=1,2,3
# print(c)
#
# # if 0:
# #     print(123)
# x = int(input("Please enter first value1: "))
# y = int(input("Please enter second value2: "))
# z = int(input("Please enter second value3: "))
# v = int(input("Please enter second value4: "))
# if (x == y==z==v):
#     print("4数相同！")
# elif (x > y):
#     if (z>x)and(y>v):
#         print("最大数为：",z)
#     elif((v>x)and(y>z)):
#         print("最大数为：", v)
#     else:
#         print("最大数为：", x)
#  elif (y > x):
#     if (z>y)and(x>v):
#         print("最大数为：",z)
#     elif((v>y)and(x>z)):
#         print("最大数为：", v)
#     else:
#         print("最大数为：", y)
#  elif (y > x):
#     if (z>y)and(x>v):
#         print("最大数为：",z)
#     elif((v>y)and(x>z)):
#         print("最大数为：", v)
#     else:
#         print("最大数为：", y)
# import copy
# a=[1,2,3]
# b=a
# c=copy.copy(a)
# d=copy.deepcopy(a)
# print(id(a))
# print(id(b))
# print(id(c))
# print(id(d))
# for i in  range(1,10):
#     for j in  range(1,10):
#         print('%s*%s=%d'%(i,j,i*j),end=',')
#     print()
# list1=[]
# for i in range(1,100):
#     if i%3==0 or i%17==0:
#         list1.append(i)
# print(sum(list1))
# num1=input('请输入一个数字')
# flag=True
# while True:
#     if type(int(num1))==int:
#         for i in range(2,num1):
#             if num1%i==0:
#                 print('%s不是素数'%num1)
#                 flag=False
#                 break
#         else:
#             print('%s是素数'%num1)
#     else:
#         print('输入错误，请重新输入')
# L=[75,98,59,81,66,43,69,85]
# for a in L:
#     if a>60:
#         print(a,end=' ')
a=1
# while a<100:
#     if a%2==1:
#         a = a + 1
#     else:
#         continue
#
# print(a)
# L = range(1,100)
# P=[]
# for a in L:
#     if a%2==1:
#         P.append(a)
# print(sum(P))
# sum=0
# n=0
# count=0
# while True:
#     n=2**count
#     count+=1
#     sum+=n
#     if count==20:
#         break
# print(sum)
# 同下list1=[i for i in range (1,100)]
# list1=[]
# for i in range (1,100):
#     list1.append(i)
# print(list1)
#元组推导 tup1=(i for i in range (1,100))
# print(tuple(tup1))
# dict1={i:j for i,j in [[1,2]]}
# print(dict1)
# print(dict(dict1))
students=['jack','tom','john','amy','kim','sunny']
for item in students:
    if item=='amy':
        print("break终止循环")
        break
    print(item)







