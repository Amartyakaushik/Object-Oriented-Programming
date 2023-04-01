# list=[23,"amartya",34,"charchil","shupnekha","lavanya","ghanshyam"]
# list.insert(3,"shailav")
# list.append(56)
# # print(list)
# # print(list[3])
# # print(list[0:4])
# # print(23 in list)
# for i in list:
#     if (i=="charchil"):
#         break;
#     # if (i=="charchil"):
#     #     continue;
#     print(i)


# tuple=(23,"amartya",34,"charchil")
# for i in tuple:
#     print(i)
# print(tuple[3])
# print(tuple[1:4])
# print(tuple.count(23))
# print(tuple.index("charchil"))

# #ONLY UNIQUE VALUE IS STORED IN SET 
# set={23,"amartya",43,"charchil",56,"shubhanya"}
# for i in set:
#     print(i)
# #print(set[1:4])    ERROR AS SET IS NOT ORDER PRESERVED
# print(set)

# marks_dict={"Amartya":11,"charchil":15,"shubhanya":29,"shupnekha":23}
# print(marks_dict["Amartya"])
# marks_dict["shupnekha"]=99
# print(marks_dict)

#                                                               #FUNCTIONS 
# def sum(first,second=3):
#     print(first+second)
# sum(234,2765)

#                                                                ##OOPS
# # CLASS VARIABLE AND INSTANCE VARIABLE
# class employee:
#     increment=1.9
#     no_of_employee=0
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
#         employee.no_of_employee+=1

#     def increased(self):
#         self.salary=self.salary*employee.increment

# print(employee.no_of_employee)
# Amartya=employee("Amartya","Kaushik",99999)
# print(employee.no_of_employee)
# Charchil=employee("Charchil","Raj",99999)
# print(employee.no_of_employee)
 
# print(Charchil.salary)
# Charchil.increased() # HERE THE CHANGE IS APPLIED TO THE INSTACE VARIABLE ONLY NOT TO THE WHOLE CLASS VARIABLE
# print(Charchil.salary)


#                                                                 # CLASS MEHTOD
# class employee:
#     increment=1.9
#     no_of_employee=0
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
#         employee.no_of_employee+=1

#     def increased(self):
#         self.salary=self.salary*employee.increment
    
#     # TO DIRECTLY CHANGE THE CLASS VARIABLE USING CLASS METHOD
#     @classmethod  ## (THIS IS CLASSMETHOD DECORATOR)
#     def change_increment(cls,amount):# HERE THE WHOLE CLASS IS PASSED AS A PARAMETER
#         cls.increment=amount

# Amartya=employee("Amartya","Kaushik",77988)
# Charchil=employee("Charchil","Raj",99888)

# print(Amartya.salary)
# employee.change_increment(3)# HERE THE CHANGE IS APPLIED TO THE WHOLE CLASS VARIABLE ONLY NOT NEEDED TO APPLY CHANGE TO THE INSTANCE ...
# Amartya.increased()
# print(Amartya.salary)


#                                                         #CLASS AS ALTERNATIVE CONSTRUCTURE...
# class employee:
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
    
#     #THIS CLASSMETHOD IS USED AS AN ALTERNATIVE CONSTRUCTURE...
#     @classmethod
#     def from_str(cls,emp_str):
#         fname,lname,salary=emp_str.split("-")
#         return cls(fname,lname,salary)
    
# Shupnekha=employee.from_str("Shupnekha-Rawat-99880")
# print(Shupnekha.__dict__)


#                                  #STATIC METHOD (WHEN NEITHER CLASS VARIABLE NOR INSTANCE VARIABLE IS NEEDED)
# class employee:
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
    
#     @staticmethod
#     def is_open(day):
#         if(day=="sunday"):
#             print(False)
#         else:
#             print(True)

# Shubham=employee("Shubham","Gill",88990)
# Shubham.is_open("monday")
# employee.is_open("sunday")


#                                                                     #INHERITENCE
# class employee:
#     increment=1.7
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary
    
# class programmar(employee):
#     def __init__(self,fname,lname,salary,prog_lang,exp):
#         super().__init__(fname,lname,salary)  # SUPER() FUNCITON IS USED TO INHERITENCE PROPERTIES FROM THE PARENT CLASS
#         self.prog_lang=prog_lang
#         self.exp=exp
    
#     def increased(self):
#         self.salary=int(self.salary*(self.increment+0.3))
#         return self.salary
# Amartya=programmar("Amartya","Kaushik",88990,"Python","6 yrs")
# print(Amartya.__dict__)
# print(Amartya.salary)
# Amartya.increased()
# print(Amartya.salary)

#                                                                 #OVERRIDING METHODS
#                                                               #DUNDER METHOD
# class employee:
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary

#     #1st 
#     def __add__(self,other):
#         return self.salary+other.salary
    
#     def __repr__(self):
#         return "Employee({},{},{})".format(self.fname,self.lname,self.salary)
    
#     def __str__(self):
#         return "The name of employee is {} {} and his salary is {}".format(self.fname,self.lname,self.salary)
    
# Amartya=employee("Amartya","Kaushik",88000)
# Charchil=employee("Charchil","Raj",88000)
# # print(Amartya+Charchil)
# # print(Amartya.__repr__())
# print(Amartya.__str__())

                                                          
#                                     #   PROPERTY DECORATOR , SETTER , DELETER... 
# class employee:
#     def __init__(self,fname,lname,salary):
#         self.fname=fname
#         self.lname=lname
#         self.salary=salary

#     @property
#     def email(self):
#         return self.fname+self.lname+"email.com"

#     @email.setter
#     def email(self,given_email):
#         name_list=given_email.split('@')[0].split('.')
#         self.fname=name_list[0]
#         self.lname=name_list[1]

# class programmar(employee):
#     def __init__(self,fname,lname,salary,prog_lang,exp):
#         super().__init__(fname,lname,salary)
#         self.prog_lang=prog_lang
#         self.exp=exp

# Amartya=employee("Amartya","kaushik",95000)
# Amartya=programmar("Amartya","Kaushik",95000,"Python","1.5 yrs")

# print(Amartya.email)
# Amartya.lname="Thakur"
# print(Amartya.email)
# Amartya.email="Thakur.Amartya@email.com"
# print(Amartya.email)
# print(Amartya.__dict__)

# #                                                            ENCAPSULATION
# class rectangle:
#     def __init__(self,length,breadth):
#         self.__length=length
#         self.__breadth=breadth

#     def set_length(self,length):
#         self.__length=length

#     def set_heigth(self,breadth):
#         self.breadth=breadth

#     def get_length(self):
#         return self.__length
    
#     def get_breadth(self):
#         return self.__breadth
    
#     def area(self):
#         return self.__length * self.__breadth
    
# rect1=rectangle(300,400)
# rect3=rectangle(322,543)

# # print(rect1.__length)
# # print(rect1.__breadth)
# # rect1.set_length(234)
# # rect1.get_length()
# print(rect1.area())
# rect1.set_length(123)
# print(rect1.get_length())

#                                                           #QUESTIONS
# #1) Take character as input from the console using input() function.Write a programm to check whether the given input is a character or a digit,if the input is 0 then exit the program, otherwise print the result.

# while True:
#     user_input=input("enter any string or digit or 0 to exit the program: ")
#     if user_input=='0':
#         print("exiting the program...")
#         break
#     elif (user_input>='a' and user_input<='z' or user_input>='A' and user_input<='Z'):
#         print("The provided input is a Character.")
#     # elif(user_input.isalpha()):
#     #     print("The provided input data is a charcter.")
#     elif (user_input.isdigit()):
#         print("The provided input is a digit .")
#     else:
#         print("Oops! Wrong input...")



# list=["alsd",345,"hdfosdhf0","rahul",34,"amartya","kaushik","charchil","raj"]
# for i in list:
#     if i=="kaushik":
#         break;
#     else: 
#         print(i)

# #2)Write a python program to count the vowels and consonants in the string,which is inputted from the user.

# string=input("enter any string: ")
# vowel_count=0
# cons_count=0
# for str in string:
#     if str in ['a','e','i','o','u','A','E','I','O''U']:
#         vowel_count+=1
#     elif str.isalpha():
#         cons_count+=1
# print(vowel_count,cons_count)

# string=input("enter any string: ")
# vowel_count=0
# cons_count=0
# if string in ['a','e','i','o','u','A','E','I','O','U']:
#     vowel_count+=1
# elif string.isalpha():
#     cons_count+=1
# print(vowel_count,cons_count)

# #3)Write a python program to convert farenthesis into celsius.The formula of farenheit conversion into celsius is: C=((farenheit-32)*5)/9.print the result.
# temp=int(input("enter the temperature in farenheit: "))
# c=((temp-32)*5)/9
# print("the temp is {0:.2f} degree celsius".format(c))

# #4)Write a python program to calculate factorial of user input data by using the recursion concept.print the result.
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# num=int(input("enter the value of num: "))
# if num<0:
#     print("oops! wrong input")
# elif num==0:
#     print("the factorial of 0 is 1")
# else: 
#     print("factorial of {} is {}".format(num,fact(num)))

# #5)Write a python program to check whether an integer is Armstron or not...
# num=int(input("enter the required input "))
# def armstrong(num):
#     sum=0
#     num_digit=len(str(num))
#     temp=num
#     while (temp!=0):
#         i=temp%10
#         sum+=i**num_digit
#         temp=temp//10
#     if sum==num:
#         print("amrstrong")
#     else:
#         print("not a armstrong")
# print(armstrong(num))
#                         #OR
# def is_armstrong(num):
#     n_digit=len(str(num))
#     temp=num
#     sum=0
#     while(temp!=0):
#         i=temp%10
#         sum+=pow(i,n_digit)
#         temp=temp//10
#     return (sum==num)
# print(is_armstrong(num))
#                         #OR
num=input("enter a number: ")
def is_armstrong(num):
    temp=num
    str_num=str(num)
    n_digit=len(str_num)
    sum=0
    for i in str_num:
        sum+=int(i)**n_digit
    return sum==num
if (is_armstrong(num)):
    print(num,"is a armstrong number.")
else:
    print(num,"is not an armstrong.")


# #6)Write a python program to enter 3*3 matrix from the console and also print transpose of it ...
# matrix=[]
  
# #7)Let's write a simple python code for function.
# #The program has a function sayhello() it takes a single argument which is a string.
# #The argument inside the paranthesis of the function is username we end the header with a colon:
# # Inside the function create a variable greet and assign a value "Hello".
# #Concatenate the variable with username and print the result. Let us look at the reusability of the funciton.
# #Let us create a list of names to whom we want to print the greeting.
# #L1['Ram','Mahesh','Vasudha','Uma','Skhar','John'] let's call the function by passing the items of the list as argument and print the result

# def sayhello(name):
#     greet="Hello"
#     return greet +" "+ name
# list=[]
# n=int(input("enter the no. of names in the list: "))
# for j in range(n):
#     name=input("enter the  no. {} name: ".format(j+1))
#     list.append(name)
# for i in list:
#     print(sayhello(i))

# # L1=['Ram','Mahesh','Vasudha','Uma','Skhar','John']
# # for i in L1:
# #     print(sayhello(i))
# # print(sayhello("amartya"))

# #8)Write a python program to check whether the user input integer is leap year is not ...
# year=int(input("enter the year uh want to check: "))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("{} is a leap year".format(year))
#         else:
#             print("Sorry,{} is not a leap year.".format(year))
#     else:
#         print("sorry, {} is not a leap year.".format(year))
# else:
#     print("Sorry,{} is not a leap year".format(year))

# #9)Write a python program to find GCD of two user input number
# num1=int(input("enter the 1st no: "))
# num2=int(input("enter the 2nd no: "))
# def GCD(a,b):
#     if b==0:
#         return a
#     else:
#         return GCD(b,a%b)
# print("The Greatest common divisor of {} and {} is {} ".format(num1,num2,GCD(num1,num2)))

# #10)Define a class person.
# #Add a method setName() which takes self and name as parameters.Inside the method,set self.name=name.
# #Add a method getName() which takes self as parameter.
# #Inside the method return self.name.Create two instance of the class person p1 and p2.
# #Take the input name from the user.Call the method setName() on p1 and pass name as parameter.Take the input name from the user.
# #Call the method setName() on p2 and pass name as parameter.
# #Call the method getName() on p1.
# #Call the method getName() on p2.
# class person:
#     def setName(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
    
# p1=person()
# p2=person()
# name1=input("enter name of p1: ")
# p1.setName(name1)
# name2=input("Enter the name of p2: ")
# p2.setName(name2)
# print("Name of p1:",p1.getName())
# print("Name of p2: ",p2.getName())