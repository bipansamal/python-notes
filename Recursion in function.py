# Recursion funciton. (when a function calls itself repeatedly.) 4*3*2*1
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)

# Example 2 its important.
def function(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * function(n-1)

print(function(5))

# RECURSION FUNCTION BY TAKING INPUT.
n = int(input("enter your recursion number"))
def function(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * function(n-1)

print(function(n))


# SIMPLE FUNCTION

def function(a,b,c):
    print("My name is",a,b)
    print("I am ",c,"years old")
a = input("enter your name :")
b = input("enter your last name :")
c = int(input("enter your age" :))

function(a,b,c)








