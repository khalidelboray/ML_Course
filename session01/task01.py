# for section in ['name','department','degree']:
#     globals()[section] = input(f"input {section.title()}: ")

name = input("Input Name: ")
department = input("Input Department: ")
degree = input("Input Degree: ")

fdegree = "Fail"
degree = int(degree)

if degree > 85:
    fdegree = "Excellent"
elif degree > 75:
    fdegree = "Very Good"
elif degree > 65:
    fdegree = "Good"
elif degree > 50:
    fdegree = "Pass"


print(f"Hello {name}, Your department is {department} and your degree is '{fdegree}'")
