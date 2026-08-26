# ==========================================
# 🧪 Student Data Analyzer
# Practice: Python Operators
# ==========================================

# ------------------------------------------
# 1️⃣ INPUT
# ------------------------------------------

name = input("Enter student name: ")
age = int(input("Enter age: "))

python_marks = float(input("Enter Python marks: "))
math_marks = float(input("Enter Mathematics marks: "))
statistics_marks = float(input("Enter Statistics marks: "))


# ------------------------------------------
# 2️⃣ ARITHMETIC OPERATORS
# ------------------------------------------

total = python_marks + math_marks + statistics_marks

average = total / 3

percentage = (total / 300) * 100

print("\n========== ARITHMETIC ==========")
print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage)


# ------------------------------------------
# 3️⃣ COMPARISON OPERATORS
# ------------------------------------------

is_adult = age >= 18

is_python_pass = python_marks >= 40
is_math_pass = math_marks >= 40
is_statistics_pass = statistics_marks >= 40

is_passing = (
    is_python_pass
    and is_math_pass
    and is_statistics_pass
)

average_pass = average >= 50

print("\n========== COMPARISON ==========")
print("Age >= 18:", is_adult)
print("Python Pass:", is_python_pass)
print("Mathematics Pass:", is_math_pass)
print("Statistics Pass:", is_statistics_pass)
print("Student is Passing:", is_passing)
print("Average >= 50:", average_pass)


# ------------------------------------------
# 4️⃣ ASSIGNMENT OPERATORS
# ------------------------------------------

bonus = 0

if average >= 80:
    bonus += 5

print("\n========== ASSIGNMENT ==========")
print("Bonus:", bonus)

final_average = average + bonus

print("Final Average:", final_average)


# ------------------------------------------
# 5️⃣ LOGICAL OPERATORS
# ------------------------------------------

scholarship = age >= 18 and average >= 80

print("\n========== LOGICAL ==========")
print("Eligible for Scholarship:", scholarship)


# ------------------------------------------
# 6️⃣ MEMBERSHIP OPERATORS
# ------------------------------------------

subjects = ["Python", "Mathematics", "Statistics"]

python_exists = "Python" in subjects
java_not_exists = "Java" not in subjects

print("\n========== MEMBERSHIP ==========")
print('"Python" in subjects:', python_exists)
print('"Java" not in subjects:', java_not_exists)


# ------------------------------------------
# 7️⃣ IDENTITY OPERATORS
# ------------------------------------------

a = subjects
b = subjects

same_values = a == b
same_object = a is b

another_subjects = ["Python", "Mathematics", "Statistics"]

same_values_again = subjects == another_subjects
same_object_again = subjects is another_subjects

print("\n========== IDENTITY ==========")

print("a == b:", same_values)
print("a is b:", same_object)

print("subjects == another_subjects:", same_values_again)
print("subjects is another_subjects:", same_object_again)


# ------------------------------------------
# 8️⃣ BITWISE OPERATORS
# ------------------------------------------

bitwise_and = age & 1
left_shift = age << 1
right_shift = age >> 1

print("\n========== BITWISE ==========")
print("Age:", age)
print("age & 1:", bitwise_and)
print("age << 1:", left_shift)
print("age >> 1:", right_shift)


# ------------------------------------------
# 9️⃣ OPERATOR PRECEDENCE
# ------------------------------------------

result1 = total + average * 2 ** 2

result2 = (total + average) * 2 ** 2

print("\n========== OPERATOR PRECEDENCE ==========")
print("total + average * 2 ** 2:", result1)
print("(total + average) * 2 ** 2:", result2)


# ------------------------------------------
# 🔟 FINAL REPORT
# ------------------------------------------

print("\n===================================")
print("       STUDENT DATA ANALYZER")
print("===================================")

print("Student Name:", name)
print("Age:", age)
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage)
print("Bonus:", bonus)
print("Final Average:", final_average)
print("Passing:", is_passing)
print("Scholarship Eligible:", scholarship)

print("===================================")