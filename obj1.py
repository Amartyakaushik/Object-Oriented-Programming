# class is the templet for the object 
#                                       INSTANT METHOD
# class employee:
#     # A constructer "def __init__" is defined to pass the parameters 
#     def __init__(self,fname,lname,salary):  # self,fname,lname,salary are the arguments 
#         self.fname=fname   # self.fname is the property name
#         self.lname=lname   # and lname is the parameter
#         self.salary=salary

# #object is the real life entity which is defined with the help of class
# Amartya=employee("Amartya","Kaushik",99000)  # after defining object further parameters is passed in it...
# Abhinav=employee("Abhinav","kaushik",99001)
# sweta=employee("sweta","kaushik",99001)
# print(Amartya.fname)
# print(Abhinav.salary)
# print(sweta.lname)




# class employee:
#     no_of_employee=0  # Initial guess is 0
#     def __init__(self,fname,lname,salary):   # Instant properties/variable...
#         self.fname=fname 
#         self.lname=lname
#         self.salary=salary
#         employee.no_of_employee+=1 # no_of_employee is increased by 1 After defining every single object(employee) 

# print(employee.no_of_employee)
# Abhinav=employee("Abhinav","kaushik",99001)
# print(employee.no_of_employee)
# sweta=employee("sweta","kaushik",99001)
# print(employee.no_of_employee)
# Amartya=employee("Amartya","Kaushik",99000) 
# print(employee.no_of_employee) 




#                                             CLASS METHOD
## Variables and instant variable
# class employee:
#     increment=1.4 #Calass variable/properties 
#     def __init__(self,fname,lname,salary):   # Instant properties/variables
#         self.fname=fname 
#         self.lname=lname
#         self.salary=salary
#         self.increment=1.8
    
#     def increased(self):
#         # self.salary=self.salary*self.increment    # When self.increment is writen then it'll check for the parameter in the instant variable/property then check for  class variable/property... 
#         self.salary=self.salary*employee.increment # Here it'll direct check for the  class Variable/property
# Amartya=employee("Amartya","Kaushik",99000)  
# Abhinav=employee("Abhinav","kaushik",99001)
# sweta=employee("sweta","kaushik",99001)

# print(Abhinav.salary)
# Amartya.increased()
# print(Amartya.salary)
# print(Amartya.__dict__) # To print all instant  class properties/variable...
# Abhinav.employee_no=33432 # To define an instant Class property/variable...
# print(Abhinav.__dict__)




##To change the Class property/Variable value as per requirement
# class employee:
#     increment=1.4 # Direct defined Class property/variable...
#     def __init__(self,fname,lname,salary):   # Instant defined Class property/variable
#         self.fname=fname 
#         self.lname=lname
#         self.salary=salary
    
#     def increased(self):
#         self.salary=self.salary*self.increment   
#         # self.salary=self.salary*employee.increment 

#     @classmethod    # class decorater is basically defined when we need to apply change in the value of any Class variable/property
#     def change_increment(cls,amount): # class is passed as argument
#         cls.increment=amount

# Abhinav=employee("Abhinav","kaushik",99001)
# sweta=employee("sweta","kaushik",99001)
# Amartya=employee("Amartya","Kaushik",99000)

# print(Amartya.salary)
# employee.change_increment(4)  # instant 
# Amartya.increased()
# print(Amartya.salary)




# #                            Class mehtod as an Alternate Constructure
# class employee:
#     def __init__(self,fname,lname,salary):
#         self.fname=fname 
#         self.lname=lname
#         self.salary=salary

# #Class as an alternative constructor
#     @classmethod
#     def str_from(cls,emp_string):
#         fname,lname,salary=emp_string.split("-")
#         return cls(fname,lname,salary)   # Calling the class constructor

# Abhinav=employee("Abhinav","kaushik",99001)
# lavanya=employee.str_from("lavanya-Bajpaye-44002")
# sweta=employee("sweta","kaushik",99001)
# Amartya=employee("Amartya","Kaushik",99000)

# print(sweta.__dict__)
# print(sweta.fname)
# print(sweta.lname)



##                                              STATIC METHOD
# class employee:
#     def __init__(self,fname,lname,salary):
#         self.fname=fname 
#         self.lname=lname
#         self.salary=salary

#     @staticmethod
#     def is_open(day):
#         if day=="sunday":
#             print(False)
#         else:
#             print(True)

# Abhinav=employee("Abhinav","kaushik",99001)
# sweta=employee("sweta","kaushik",99001)
# Amartya=employee("Amartya","Kaushik",99000)
# print(sweta.is_open("monday"))




##                                        INHERITENCE
class employee:  # Parent Class
    # increment=3.5
    def __init__(self,fname,lname,salary):
        self.fname=fname 
        self.lname=lname
        self.salary=salary

class faculty(employee):   # Child class 
    increment=4.5
    def __init__(self,fname,lname,salary,proglang,exp):
        super().__init__(fname,lname,salary) # The "super()" is used to call the arguments from the parent class
        self.proglang=proglang  # new parameters are being passed...
        self.exp=exp

    def increased(self):  # Defining an extra Class variable
        self.salary=self.salary+self.increment
        
Abhinav=employee("Abhinav","kaushik",99001)
sweta=employee("sweta","kaushik",99001)
Amartya=employee("Amartya","Kaushik",99000)
Lavanya=faculty("Lavanya","Bishnoi",444444,"C++","4 yrs")

print(Abhinav.__dict__)
print(Lavanya.__dict__)
Lavanya.increased()
print(Lavanya.salary)
print(help(faculty))           ##"help()" function gives the whole detail about all the functions and the methods used in the code running



