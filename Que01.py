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

def fun(i,j,k):
    # while i<=j:
    for x in range(i,j):
            guess=0
            while x<=j:
                f=(x%10)*10+(x//10)
                if (x+f)%k==0:
                     guess+=1
    print(guess)
print(fun(10,20,2))
   

