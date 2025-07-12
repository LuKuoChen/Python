#如何使用數字、數字的用法
print(77)
print(77.2)
print(-77.2)
print(8+5)
print(8-5)
print(8*5)
print(8/5)
print(8//5) #整數除法
print(8+8*5) #符合四則運算
number=8
print(number*5)
print(8%5) #取餘數

#函式 function
number=8
# print("會印出數字"+number)  文字不能+數字
print(str(number))
print("會印出數字"+str(number))

number=-8
print(abs(number))
number=2
print(pow(number,4))

print(max(100,2,-5,500,8,4,75,95,6,761))
print(min(100,2,-5,500,8,4,75,95,6,761))

print(round(4.4))
print(round(4.6))
print(round(3.1415926,2))

from math import *
print(floor(4.4)) #無條件捨去
print(floor(4.6))

print(ceil(4.4)) #無條件進位
print(ceil(4.6))

print(sqrt(64)) #開根號
print(sqrt(36))