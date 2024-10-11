# # oops in pythan
# # to map with real world scenarios, we started using objects in code.
# # this is called object oriented programming. 
class Student:
    name = ("nishan")
    
s1 = Student()
print(s1.name)


# class car:

#     color = "blue"
#     brand = "mercedes"
#     model = 2014


# car1 = car()
# print(car1.color)
# print(car1.brand)
# print(car1.model)

# # constructor or init function.
# # All classes have a function called _init_(), which is allways executed when the class is being initiated.

# # pratice 
# # create student class that takes name & marks of 3 subject as arguments in constructor. 
# # Then create a method to print average.

class student:
    def __init__( self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi", self.name, "your avg score is:", sum/3)    

s1 = student("tony stark", [99, 98, 97])
s1.get_avg()    


# # important
# Abstraction(private garny) 
class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car start..")

car1 = car()
car1.start()

# # Encapsulation  Encapulation(data ra function hunx object vitra tai Encapulation ho)
# # wrapping data and functions into a single unit(object).


# # lets pratice 
# # create account class with 2 attributes - balance & account no. create method for debit, credit & printing thte balance

class account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    #debit method 
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debit")
        print("total balance = ", self.get_balance())


    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credit")
        print("total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance

acc1 = account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)



