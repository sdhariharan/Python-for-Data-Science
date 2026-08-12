# Get student information
name = input("Enter name: ")
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
department = input("Enter department: ")
college = input("Enter college: ")

# Student Performance Report
print("\n========================================")
print("\tSTUDENT PERFORMANCE REPORT")
print("========================================")

print(f"Name       : {name}")
print(f"Age        : {age}")

# Using sep
print("Department", department, sep=" : ")
print("College", college, sep=" : ")

print(f"CGPA       : {cgpa:.2f}", end="\n")

print("========================================")

# Data Types
print("\nData Types:")

print(f"Name       → {type(name)}")
print(f"Age        → {type(age)}")
print(f"CGPA       → {type(cgpa)}")
print(f"Department → {type(department)}")
print(f"College    → {type(college)}")