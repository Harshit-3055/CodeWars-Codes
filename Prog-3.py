""""
Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!

"""
import random
a = int(input("Enter the value of a = "))
b = int(input("Enetr the value of b = "))
sum = 0
if(a==b):
    print(a)
elif(a>b):
    for i in range(b,a+1):
        sum = sum + i
elif(b>a):
    for i in range(a,b+1):
        sum = sum + i
if(a!=b):
    print("Sum = ", sum)