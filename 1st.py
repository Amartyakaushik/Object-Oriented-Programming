list=[23,"amartya",34,"charchil","shupnekha","lavanya","ghanshyam"]
list.insert(3,"shailav")
list.append(56)
print(list)
print(list[3])
print(list[0:4])
print(23 in list)
for i in list:
    # if (i=="lavanya"):
    #     break;
    if (i=="charchil"):
        continue;
    print(i)


tuple=(23,"amartya",34,"charchil")
for i in tuple:
    print(i)
print(tuple[3])
print(tuple[1:4])
print(tuple.count(23))
print(tuple.index("charchil"))

ONLY UNIQUE VALUE IS STORED IN SET 
set={23,"amartya",43,"charchil",56,"shubhanya"}
for i in set:
    print(i)
#print(set[1:4])    ERROR AS SET IS NOT ORDER PRESERVED
print(set)

marks_dict={"Amartya":11,"charchil":15,"shubhanya":29,"shupnekha":23}
print(marks_dict["Amartya"])
marks_dict["shupnekha"]=99
print(marks_dict)

def sum(first,second=3):
    print(first+second)
sum(234,2765)


# CLASS VARIABLE AND INSTANCE VARIABLE
class employee:
    increment=1.9
    no_of_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        employee.no_of_employee+=1

    def increased(self):
        self.salary=self.salary*employee.increment

print(employee.no_of_employee)
Amartya=employee("Amartya","Kaushik",99999)
print(employee.no_of_employee)
Charchil=employee("Charchil","Raj",99999)
print(employee.no_of_employee)
 
print(Charchil.salary)
Charchil.increased() # HERE THE CHANGE IS APPLIED TO THE INSTACE VARIABLE ONLY NOT TO THE WHOLE CLASS VARIABLE
print(Charchil.salary)

# CLASS MEHTOD
class employee:
    increment=1.9
    no_of_employee=0
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        employee.no_of_employee+=1

    def increased(self):
        self.salary=self.salary*employee.increment
    
    # TO DIRECTLY CHANGE THE CLASS VARIABLE USING CLASS METHOD
    @classmethod  ## (THIS IS CLASSMETHOD DECORATOR)
    def change_increment(cls,amount):# HERE THE WHOLE CLASS IS PASSED AS A PARAMETER
        cls.increment=amount

Amartya=employee("Amartya","Kaushik",77988)
Charchil=employee("Charchil","Raj",99888)

print(Amartya.salary)
employee.change_increment(3)# HERE THE CHANGE IS APPLIED TO THE WHOLE CLASS VARIABLE ONLY NOT NEEDED TO APPLY CHANGE TO THE INSTANCE ...
Amartya.increased()
print(Amartya.salary)

#CLASS AS ALTERNATIVE CONSTRUCTURE...
class employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    #THIS CLASSMETHOD IS USED AS AN ALTERNATIVE CONSTRUCTURE...
    @classmethod
    def from_str(cls,emp_str):
        fname,lname,salary=emp_str.split("-")
        return cls(fname,lname,salary)
    
Shupnekha=employee.from_str("Shupnekha-Rawat-99880")
print(Shupnekha.__dict__)

#STATIC METHOD (WHEN NEITHER CLASS VARIABLE NOR INSTANCE VARIABLE IS NEEDED)
class employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
    @staticmethod
    def is_open(day):
        if(day=="sunday"):
            print(False)
        else:
            print(True)

Shubham=employee("Shubham","Gill",88990)
Shubham.is_open("monday")
employee.is_open("sunday")

#INHERITENCE
class employee:
    increment=1.7
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
    
class programmar(employee):
    def __init__(self,fname,lname,salary,prog_lang,exp):
        super().__init__(fname,lname,salary)  # SUPER() FUNCITON IS USED TO INHERITENCE PROPERTIES FROM THE PARENT CLASS
        self.prog_lang=prog_lang
        self.exp=exp
    
    def increased(self):
        self.salary=int(self.salary*(self.increment+0.3))
        return self.salary
Amartya=programmar("Amartya","Kaushik",88990,"Python","6 yrs")
print(Amartya.__dict__)
print(Amartya.salary)
Amartya.increased()
print(Amartya.salary)

#DUNDER METHOD
class employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    #1st 
    def __add__(self,other):
        return self.salary+other.salary
    
    def __repr__(self):
        return "Employee({},{},{})".format(self.fname,self.lname,self.salary)
    
    def __str__(self):
        return "The name of employee is {} {} and his salary is {}".format(self.fname,self.lname,self.salary)
    
Amartya=employee("Amartya","Kaushik",88000)
Charchil=employee("Charchil","Raj",88000)
# print(Amartya+Charchil)
# print(Amartya.__repr__())
print(Amartya.__str__())


#PROPERTY DECORATOR , SETTER , DELETER...
class employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    @property
    def email(self):
        return self.fname+self.lname+"email.com"

    @email.setter
    def email(self,given_email):
        name_list=given_email.split('@')[0].split('.')
        self.fname=name_list[0]
        self.lname=name_list[1]

class programmar(employee):
    def __init__(self,fname,lname,salary,prog_lang,exp):
        super().__init__(fname,lname,salary)
        self.prog_lang=prog_lang
        self.exp=exp

Amartya=employee("Amartya","kaushik",95000)
Amartya=programmar("Amartya","Kaushik",95000,"Python","1.5 yrs")

print(Amartya.email)
Amartya.lname="Thakur"
print(Amartya.email)
Amartya.email="Thakur.Amartya@email.com"
print(Amartya.email)
print(Amartya.__dict__)