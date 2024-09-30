# Variables
# Variables are containers for storing data values
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

# CHECKING THE WHICH VARIABLES IT IS.
x = 5
y = "John"
print(type(x))
print(type(y))

# WE CAN STORE MULTIPLE VALUE IN ONE VARIABLES.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Python - Output Variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


#Global Variables
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
#Global variables can be used by everyone, both inside of functions and outside.

# FOR EXAMPLE .
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

# EXAMPLE .2
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# EXAMPLE
a = "Hello, World!"
print(a[1])

# Python - Slicing Strings
# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# ExampleGet your own Python Server
# Get the characters from position 2 to position 5 (not included):
# Example
b = "Hello, World!"
print(b[2:5])

# Example 2
b = "Hello, World!"
print(b[-5:-2])

# ITS Concatenatin ("hello" + "world") its adding two words
str1= ("Mero")
str2=("College")
print(str1+str2)

# FOR EXAMPLE 2.
str1="Temro:"
str2="school"
print(str1+str2)
print(len(str1+str2))

# Length of string  len(str)
str1="hamro"
print(str1)
print(len(str1))
print(type(str1))

## Multiline Comments
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")


# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.

# Upper Case and lowercase
# ExampleGet your own Python Server
# The upper() method returns the string in upper case:

a = "Hello, World!"
print(a.upper())
print(a.lower())


# Replace String
# Example
# The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("H", "J"))


# F-Strings
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
# Example
# Create an f-string:

age = 20
txt = f"My name is John, I am {age} years old"
print(txt)

# Example 2
txt = f"The price is {20 * 59} dollars"
print(txt)


# THIS IS EXAMPLE OF /n TO TAKING IN HORIZONTAL TO VERTICAL.
txt = "Hello\rWorld!"
print(txt) 



# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	

# Change Item Value in LIST
# To change the value of a specific item, refer to the index number:
# ExampleGet your own Python Server
# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Example 2
# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)


# Append Items (adding append value to the end)
# To add an item to the end of the list, use the append() method:

# ExampleGet your own Python Server
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Insert Items (only insert and cannot delete value)
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:

# Example
# Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend List (creating all itmes in same line)
# To append elements from another list to the current list, use the extend() method.
# Example
# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Remove Specified Item
# The remove() method removes the specified item.
# ExampleGet your own Python Server
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Example 2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
