
#  multiplication table by using while loop.
i = 1
n = int(input("enter your number"))
while i <= 10:
    print(i*n)
    i += 1

# multiplication table by using for loop.
n = int(input("enter the number"))
for i in range(1, 11):
    print(i*n)

# MULTABLE TABLE OF ANY GIVEN NUMBER BY USER.
num = int(input("enter your number"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

# odd number of 10. by using for loop.
for i in range(1,10,2):
    print(i)

# # even number of 10. by using for loop.
for i in range(2,10,2):
    print(i)
    continue
print(i)
i == 10


# FULL MULTIPLICATION TABLE FROM 1 TO 12 

def print_multiplication_tables(start=1, end=12, max_multiplier=10):
    # Header
    header = "\t".join([f"Table of {i}" for i in range(start, end + 1)])
    print(header)
    
    # Generating the tables
    for i in range(1, max_multiplier + 1):
        row = []
        for j in range(start, end + 1):
            row.append(f"{j} × {i} = {j * i}")
        print("\t".join(row))

# Print multiplication tables for numbers 1 to 12
print_multiplication_tables()
