# CONVERTOR PERCENTAGE INTO GRADE
mark = float(input("enter your grade:"))

if (mark >= 101):
    grade = "not valid"
    

elif (mark >= 90):
    grade = "A+"

elif(mark >= 80):
    grade = "A"

elif(mark >= 70):
    grade = "B+"

elif(mark >= 60):
    grade = "B"

elif(mark >= 50):
    grade = "C+"

elif(mark >= 40):
    grade = "C"

elif(mark >= 30):
    grade = "D"

elif(mark >=20):
    grade = "NG"

print("grade of the sutdent ->",grade)

# CONVERTOR GPA INTO PERCENTAGE

GPA =float(input("enter your gpa :"))
per = (GPA / 4.0) * 100

print(f"YOU Have :{per}%")


# CONVERTOR PERCENTAGE INTO GPA
percentage =float(input("enter your percentage :"))
gpa = (percentage / 100) * 4.0
print(f"YOU Have :{gpa}")
