name = "Hariharan"
age = "20"
cgpa = "8.27"
attendance = "92"
is_placed = "False"

# Type conversion
age = int(age)
cgpa = float(cgpa)
attendance = int(attendance)
is_placed = is_placed == "True"

# Calculate remaining attendance
remaining_attendance = 100 - attendance

# Print values and their types
print(f"Name: {name} | Type: {type(name)}")
print(f"Age: {age} | Type: {type(age)}")
print(f"CGPA: {cgpa} | Type: {type(cgpa)}")
print(f"Attendance: {attendance} | Type: {type(attendance)}")
print(f"Placed: {is_placed} | Type: {type(is_placed)}")
print(f"Remaining Attendance: {remaining_attendance}")