# # print('*')
# # print("***")
# # print("****")
# # print("*****")
# # print("******")

# name = input(print("enter your name "))
# name = input("enter your name: ")

# i = 1
# while i <= 100:
#     print ("my name is :", name)
#     i += 1

# # #Break and continue
# # #break: used to terminate the loop when encountered.
# # #for example 
# i = 1
# while i <= 5:
#     print(i)
#     if(i== 3):
#         break
#     i += 1
    

# num = [1,4,9,16,25,36,49,81,100]
# x = 36
# i = 0
# while i < len(num):
#     if(num[i] == x):
#         print("Found at idx",i)
#         break
#     else:
#         print("Finding")
#     i += 1
# print("end of loop")
# # #  Continue
# # # continue: terminate execution in the current iteration & continue execution of the loop with the next iteration
# # # for example
# i = 0
# while i <= 5:
#     if(i== 3):
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

# # for eg.
# i = 1
# while i <= 10:
#     if(i%2== 0): # formula for odd number
#         i += 1
#         continue #skip
#     print(i)
#     i += 1
# # # for eg.
# i = 1
# while i <= 10:
#     if(i%2 != 0): # formula for even number.
#         i += 1
#         continue #skip
#     print(i)
#     i += 1

# example of for loop 
# list = (1,2,3,4,5)

# for i in list:
#     print(i)
# example of forloop

# for i in range(11):
#     if i == 0:
#         continue
#     print(i)

# # # for eg
# # num = ( "banana", "mango", "apple")
# # for i in num:
# #     print(i)


# sum = (23,23,34,45,56,76)

# for i in sum:
#     print(i)

# # # Eg of range.
# num = range(5)

# for i in num:
#     print(i+1)

# # # eg.
# for i in range(10):
#     print(i)

# # to print even number.
# for i in range(2,100,2):
#     print(i)

# # # to print odd number.
# # for i in range(1,100,2):
# #     print(i)

# # # for i in range(101):
# #     print(i)
#    #table of 15
n = int(input("enter the number"))
for i in range( 1, 11):
    print(n*i)
 # table of 6
num = int(input("enter the num"))
for i in range(1,11):
    print(num,"*",i, "=",num*i)

# # # Pass loop.
# # for i in range(5):
# #     pass


# # print("some useful work")


# # Function in pythan.  (function ma repat huny code lai leykhanu sakinx)
# # for example.

# # a = 3
# # b = 5
# # sum = a+b
# # print(sum)

# # # more line of code
# # a = 54
# # b = 76
# # sum = a + b
# # print(sum)
# # perfect example of function.

# # def calc_sum(a ,b):
# #     sum = a + b
# #     print(sum)
# #     return sum

# # calc_sum(5,5)
# # calc_sum(45,56)

# # another example of function defination
# # def calc_sum(a,b):#parameters
# #     return a + b
# # sum = calc_sum(1,4)# function call; argument
# # print(sum)

# # def print_hello():
# #     print("hello")
# # print_hello()
# # print_hello()
# # print_hello()
# # print_hello()

# # # types of function 
# # #there are two type function . built in function, user define function

# # print("apna college", end=" ")
# # print("hero man")

# # #Default parameter.
# # #Assigning a defult value to parameter, which is used when no argument is passed. 
# # def cal_prod(a,b):
# #     print(a *b)
# #     return a * b

# # cal_prod(2)

# # enter your name: Bipan
# # enter your last name: Samal
# # your name is Bipan Samal
# # 
# # using function


# # cities = ["kathmandu", "gaighat", "murkuchi"]

# # def print_len(list):
# #     print(len(list))

# # def print_list(list):
# #     for item in list:
# #         print(item, end=" ")
    

# # print_list(cities)
# # print()


# # def cal_fact(n):
# #     fact = 1
# #     for i in range(1, n+1):
# #         fact *= 1
# #         print(fact)
# #     cal_fact(6)     
        
# # convert USD to npr


# # # covert USD to ipr
# # def convertor(usd_val):
# #     inp_val = usd_val * 86
# #     print(usd_val, "USD =", inp_val, "INp")

# # convertor(1)
# # def letter(name):
# #     return
# # string1 = (input("enter your name :"))
# # string2 = (input("enter your last name :"))
# # print("my name is",string1,string2)

# # def printname(s1,s2):
# #     print("my name is ",s1,s2)
# # s1 = input("enter your name:")
# # s2 = input("enter your last name:")
# # printname(s1,s2)

# # def printname (s1,s2):
# #     print("my name is",s1,s2)
# # s1 = input("enter your name:")
# # s2 = input("enter your last name:")


    

# def convertUsdToNpr(usd_val):
#     npr_val = usd_val * 133.46
    
#     print(usd_val, "USD = ", npr_val, "NPR")


# amount = int(input("enter your amount: "))
# convertUsdToNpr(amount)


def convertNprToUsd(npr_val):
    usd_val = npr_val / 133.46
    
    print(npr_val, "NPR = ", usd_val, "USD")


amount = int(input("enter your amount: "))
convertNprToUsd(amount)




