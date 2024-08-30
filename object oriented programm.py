# del keybord 
# used to delete object properties or object itself.
# for example .
# class student:
#     def __init__(self,name):
#         self.name = name

# s1 = student ("shradha")
# print (s1.name)
# del s1.name
# print (s1.name)

# private (like) attributes & methods
# conceptual Implementation in python
# private attributes & method are meant to be used only with the class and aren't accessible from outside the class
# for example

# class Account:
#     def __init__(self, acc_no, acc_pass ):
#         self.acc_no = acc_no
#         self.acc__pass = acc_pass

# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)

# foe example
# class person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")
        
#     def welcome(self):
#         self.__hello()

# p1 = person()

# print(p1.welcome())

# Inherintance(liny kam garx)
# when one class(child/derived) derives the properties & method of another class(parent/base).

# for example
# class car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car start..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class Toyotacar(car):
#     def __init__(self, name):
#         self.name = name

# car1 = Toyotacar("fortuner")
# car1 = Toyotacar("prius")

# print(car1.color)
        

# inherintance types , single inherintance, Multi-level inherintance, multiple inherintance
# class car:
#     @staticmethod
#     def start():
#         print("car start..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class Toyotacar(car):
#     def __init__(self, brand):
#         self.brand = brand

# class Fortuner(Toyotacar):
#     def __init__(self, type):
#         self.type = type

# car1 = Fortuner("diesel")
# car1.start()


# for example
# class A:
#     varA = "wellcome to class A"

# class B:
#     varB = "wellcome to class B"

# class C(A, B):
#     varC = "wellcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varA)
# print(c1.varB)


# super method
# super()method is used to access methods of the parent class,

# class car:
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("car start..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class Toyotacar(car):
#     def __init__(self, name, type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = Toyotacar("prius", "electric")
# print(car1.type)

# Class method
# A class method is bound to the class & recives the class as an implicit first argument
# Note - static method cann't access or modify class state & generally for utility

# class student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = student(98, 97, 99)
# print(stu1.percentage)

# example.of property
# class student:
#     def __init__(self, phy, chem, math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    
# stu1 = student(98, 97, 99)
# print(stu1.percentage)
       
# stu1.phy = 86
# print(stu1.percentage)


# polymorphism : operator overloading
# when the same operator is allowed to have different meaning according to the context.
 # for example

# print(1 + 3) #4
# print("bipan" + "magar")
# print([1, 2, 3] + [4, 5, 6])

# complex number operator & Dunder function( __add__). this is  dunder function

# class complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
    
#     def shownumber(self):
#         print(self.real,"i +", self.img,"j")

#     def add(self,num2):
#         newreal = self.real + num2.real
#         newimg = self.img + num2.img
#         return complex(newreal,newimg)

# num1 = complex(1, 3)
# num1.shownumber()

# num2 = complex(4, 6)            
# num2.shownumber()

# num3 = num1.add(num2)
# num3.shownumber()

# Define  a Employee class with attributes role, department & salary. This class has also showsetails()method

class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    
    def showdetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

e1 = Employee("accountant", "finance", "60,000")
e1.showdetails()