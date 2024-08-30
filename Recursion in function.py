# Recursion funciton. (when a function calls itself repeatedly.)
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

def printname (s1,s2,s3):
    print("my name is",s1,s2,)
    print("I am",s3,"years old")
    # print("i live in",s4)
    # print("i read in",s5)

s1 = input("enter your name:")
s2 = input("enter your last name:")
s3 = input("enter your age:")
printname(s1,s2,s3)


# def printname (q1,q2,q3):
#     print("my age is",q1)
#     print("i am",q2)
#     print("i love",q3)

# q1 = input("enter your age:")
# q2 = input("enter your passion:")
# q3 = input("enter your ideal:")
# printname(q1,q2,q3)


# files (there are two tpyes of file)
# files can be used to perform operations on a file. (read & write data)
# types of all file
# 1) Text file : .txt, .docx, .log etc.
# 2) Binary file : .mp4, .mov, .png, .jpeg etc.

# f = open("demo.txt", "r")

# data = f.read()
# f.close()

# print(data)

f = open("demo.txt", "r")
data = f.read()
f.close()
print(data)



