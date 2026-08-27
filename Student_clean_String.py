import re

student = "  hariharan kumar  "
email = "HARIHARAN@GMAIL.COM"
skills = "Python,Pandas,NumPy,SQL"
marks = "Python:85,SQL:90,Statistics:78"

# 1. Clean the name
name = student.strip().title()

print("Clean Name:", name)

# 2. Indexing
print("First character:", name[0])
print("Last character:", name[-1])

# 3. Slicing
print("First 4 characters:", name[:4])
print("Last 4 characters:", name[-4:])
print("Reversed name:", name[::-1])

# 4. Email processing
email = email.lower()
print("Email:", email)
print("Does it end with .com?", email.endswith(".com"))

# 5. Skills
skill_list = skills.split(",")
skill_string = " | ".join(skill_list)

print("Skills List:", skill_list)
print("Skills:", skill_string)

# 6. Searching
print('Does the name contain "Hari"?', "Hari" in name)
print('How many times does "a" appear?', name.lower().count("a"))

# 7. Marks using Regex
mark_list = re.findall(r"\d+", marks)

print("Marks:", mark_list)

# 8. Final formatted output
print("\n--- Student Details ---")
print(f"Student: {name}")
print(f"Email: {email}")
print(f"Skills: {skill_string}")
print(f"Marks: {', '.join(mark_list)}")