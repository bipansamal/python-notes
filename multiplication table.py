# #This is multiplication table of 1 to 12.

# def printmultiplication(start, end):
#     # Create a list to store the results
#     table = []

#     # Fill the table with formatted results
#     for i in range(start, end + 1):
#         row = [f"{i} * {j} = {i * j}" for j in range(start, end + 1)]
#         table.append(row)

#     # Print the table in a vertical format
#     # Calculate the maximum length of the items in the column
#     col_width = max(len(item) for row in table for item in row)

#     for j in range(len(table[0])):
#         # Print each column
#         for i in range(len(table)):
#             print(f"{table[i][j]:{col_width}}", end='  ')
#         print()

# printmultiplication(1, 10)


# This is also multiplication table by taking input of any number...and to give function.
# its important to give input.
# def print_num(start,end):
#      return 

# num = int(input("enter your number"))
# for i in range(1,11):
#      print(num,"*",i, "=", num*i)
    



# final i made a function in multiplication table.
# def print_name(a,b):
#      return
# a = int(input("enter your num"))
# b = int(input("table you want"))

# for i in range(1,b+1):
#           print(a,"*",i, "=",a*i)
          

     
# # multiplication table ..
# def print_num(start,end):
#     return
# num = int(input("enter the number:"))
# tableNum = int(input("how many table do you want?"))
# for i in range(1,tableNum+1):
#     print(num,"*",i,"=",num*i)




# # Print the multiplication table of an number n and creating a triangle
# def print_num(start,end):
#     return
# i = 1
# n= input("enter the number")
# while i<= 5:
#     print(i*n)
#     i += 1

# # # the multiplication table of any number n.
# def print_num(start,end):
#     return
# i = 1
# n= int(input("enter the number"))
# while i<= 10:
#     print(i*n)
#     i += 1

# def multi_table(a,b):
#     return
# a = int(input("enter your number"))
# b = int(input("how many table do you want?"))

# for i in range(1,b+1):
#     print(a, "*",i, "=", a*i)




# def print_num(a,b):
#     return a + b
# sum = print_num(5,9)
# print(sum)




# def greet(name="Guest"):
#     print(f"Hello, {name}!")

# greet()
# greet("Alice")

def print_num(numbers):
    return min(numbers), max(numbers)
result = print_num([2,3,1,4,5])
print(result)