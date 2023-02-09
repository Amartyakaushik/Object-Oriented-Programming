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


b=int(input("num: "))
for i in range(b):
        y = True
        if(str(i) == str(i)[::-1]):
            if(i>2):
                for a in range(2,i):
                    if(i%a==0):
                        y = False
                        break
                    if y:
                        print(i)