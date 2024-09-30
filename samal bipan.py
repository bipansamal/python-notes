## To adding numbers in vertical.
sum = (2,3,4,5,6,7,8,9)
i=0
while i < len(sum):
    print(sum [i])
    i+= 1

## To Finding number . by using if else condition..
num = [1,4,9,16,25,36,49,81,100]
x = 36
i = 0
while i < len(num):
    if(num[i] == x):
        print("Found at idx",i)
    else:
        print("Finding")
    i += 1

## multi table ..
count = int(input("enter your number"))
num = int(input("how many table do you want"))
for i in range(1,num+1):
    print(count,"*",i, "=",count * i)

