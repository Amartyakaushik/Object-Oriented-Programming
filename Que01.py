# i=34
# j=(i%10)*10+(i//10)
# print(j)

# guess=0
# def fun(i,j,k):
#     for x in range(i,j):
#         f=(i%10)*10+(i//10)
#         if (i+f)/k==0:
#             return i
#         else:
#             False
# print(fun(1,10,2))

# def fun(i,j,k):
#     for x in range(i,j):
#         guess=0
#     # while i<=j:
#         f=(x%10)*10+(x//10)
#         if (x+f)%k==0:
#             guess+=1
#     return guess
# print(fun(10,20,2))

# def fun(i,j,k):
#     # while i<=j:
#     for x in range(i,j):
#             guess=0
#             f=(x%10)*10+(x//10)
#             while x==f:
#                 if (x-f)%k==0:
#                     guess+=1
#     print(guess)
# print(fun(10,20,2))

#                                                      #1
# cont=[int(x) for x in input().split()]
# cnt1=cnt2=cnt3=0
# for i in cont:
#     if i%2==0:
#         cnt1+=1
#     if i%5==0:
#         cnt2+=1
#     if i%7==0:
#         cnt3+=1

# dc={2:cnt1,5:cnt2,7:cnt3}
# print(dc)

#                                                        #2
# sday=int(input())
# smon=int(input())
# syr=int(input())
# eday=int(input())
# emon=int(input())
# eyr=int(input())
# print("{}/{}/{}".format(sday,smon,syr),"to","{}/{}/{}".format(eday,emon,eyr))
# l1=[]
# l2=[]
# for i in range(syr,eyr):
#     if i%4==0:
#         l1.append(i)
#     if i%4!=0:
#         l2.append(i)
# print(l1)
# print(l2)

#                                                  #3
# n=int(input("number: "))
# for i in range(2,n+1):
#     if n%i==0:
#         flag=True
#     else:
#         nprime=False
# if str(n)==str(n)[::-1] and  nprime:
#     print("yes it")


# b=int(input("num: "))
# for i in range(b):
#         y = True
#         if(str(i) == str(i)[::-1]):
#             if(i>2):
#                 for a in range(2,i):
#                     if(i%a==0):
#                         y = False
#                         break
#                     if y:
#                         print(i)


##SS234
# import math
# a=float(input("opposite: "))
# b=float(input("hypotemous: "))
# c=a/b
# x=math.asin(c)  # To find in inverse of sin
# deg=math.degrees(x)
# print("{0:.2f}".format(deg))

##SS235
# import math
# n=float(input("angle: "))
# print("{0:.2f}".format(math.tan(math.radians(n))))

#SS236
# import math
# side1=float(input("side1: "))
# side2=float(input("side2: "))
# hyp=math.sqrt((side1**2+(side2)**2))
# print(hyp**3)

##SS237
# import math
# n=int(input("n: "))
# print("{0:.3f}".format(math.pi**n))

##SS238
# import math
# w=10
# a=int(input("Amplitude: "))
# t=int(input("time: "))
# xt=a*(math.sin(w*t))
# print("electromagnetic wave (xt) : {:.4f}".format(xt))

# ##239
# import math
# f=float(input("f: "))
# print("{:.4f}".format(math.acos(f)))

##240
# import math
# y=int(input("y: "))
# x=math.radians(y)
# cosec_x=1/math.sin(x)
# sec_x=1/math.cos(x)
# cot_x=1/math.tan(x)
# print("{0:.2f}".format(cosec_x))
# print("{0:.2f}".format(sec_x))
# print("{0:.2f}".format(cot_x))

## DEF QUESTIONS
##265
# def minimum(x,y,z):
#     a=max(x,y,z)
#     b=min(x,y,z)
#     q=x+y+z-(a+b)
#     return q
# x=int(input("X: "))
# y=int(input("Y: "))
# z=int(input("Z: "))
# print(minimum(x,y,z))

##266
# def is_prime(year):
#     if year%100==0:
#         if year%400==0:
#             print(366*24*60*60)
#     elif year%4==0:
#         print(366*24*60*60)
#     else:
#         print(-1)
# year=int(input("year: "))
# is_prime(year)

#269                                 doubt
# x=int(input("x: "))
# y=int(input("y: "))
# def perfect_cube(x,y):
#     for i in range (x,y):
#         j=i**1/3
#         if round(j**3)==i:
#             print(i)
#         # else:
#         #     print("empty")
# perfect_cube(x,y)
            
##270
# string=str(input("str: "))
# def constants(string):
#     b=''
#     a=0
#     for i in string:
#         if i in ["a","e",'i','o','u','A','E','I','O','U']:
#             continue
#         else:
#             b+=i
#             a+=1
#     if a==0:
#         print("Empty")
#     else:
#         print(b)
# constants(string)

##271
n=int(input("n: "))
def num_base_five(n):
    j=str(n)
    for i in len(j)+1:
        j[-i]=(5**(i-1))*i
        print(j)
num_base_five(n)
        