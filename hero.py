# print the number from 0 to 5 using(while loop).
i=0
while i<=5:
    print(i)
    i+= 1

# print the number from 5 to 0 using(while loop)
i=5
while i>=0:
    print(i)
    i-= 1

# print the("my name is bipan magar") using while loop
i = 1
while i<= 5:
    print("my name is bipan magar")
    i += 1

# print the multiplication table of a number n.
n = int(input("enter the number:"))
i=1
while i<= 10:
    print(n*i)
    i+= 1

# print the multipliction table of 17 number.
n=17
i=1
while i<= 10:
    print(n*i)
    i+= 1

# Print the element of the following list using a loop: {1,4,9,16,25,36,49,81,100}
elements = [1,4,9,16,25,36,49,81,100]
i = 0
while i < len(elements):
    print(elements[i])
    i += 1

num = [1,4,9,16,25,36,49,81,100]
x = 36
i = 0
while i < len(num):
    if(num[i] == x):
        print("Found at idx",i)
    else:
        print("Finding")
    i += 1

 