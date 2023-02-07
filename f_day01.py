# # A simple Python function
# def fun():
# 	print("Welcome to GFG")

# # Driver code to call a function
# fun()


## Sum of two numbers
# num2=int(input("num2 : "))
# num1=int(input("num1 : "))
# def add(num1: int,num2: int) -> int:
#     num3=num1+num2
#     return num3
# sum=num2+num1
# print(f"sum of {num1} and {num2} is {sum}")


# #To find prime numbers
# def is_prime(num):
#     if num in [2,3]:
#         return True
#     if (num==1) or (num%2==0):
#         return False
#     r=3
#     while r*r <= num:
#         if num%r==0:
#             return False
#         r+=2
#         return True
    
# print(is_prime(47))


# # To check if the number is even or odd
# def even_odd(num):
#     if num%2==0:
#         return "is even"
#     else:
#         return "is odd"
    
# print(34,even_odd(34))


#                                             #TYPES OF FUNCTION ARGUMENTS 

#                                        # Default argument
# def myfun(x,y=44): 
#     print("x: ", x)
#     print("y: " ,y)

# myfun(34)   # it assumes a default value if a value is not provided in the function call for that argument.

#                                          # keyword argument
# def student(fname,lname):
#     print(fname,lname)
# student(fname="Amartya",lname="Kaushik")

#                                          # Variable-length argument
# def my_list(*list):                                 *args (Non-Keyword Arguments)
#     for arg in list:
#         print(arg)

# my_list("Amartya","kaushik","age: 19","male")

def myfun(**args):
    for key,value in args.items():
        print("%s == %s"% (key,value))

myfun(first="Amartya",mid="singh",last="Rajput")