# Student Data Analyzer


def calculate_total(marks):
    """Return the total of all marks."""
    return sum(marks)


def calculate_average(marks):
    """Return the average of all marks."""
    return sum(marks) / len(marks)


def find_highest(marks):
    """Return the highest mark."""
    return max(marks)


def find_lowest(marks):
    """Return the lowest mark."""
    return min(marks)


def calculate_grade(average):
    """Return the grade based on the average mark."""

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def student_report(name, *marks, course="Data Science"):
    """Generate and print the complete student report."""

    total = calculate_total(marks)
    average = calculate_average(marks)
    highest = find_highest(marks)
    lowest = find_lowest(marks)
    grade = calculate_grade(average)

    # Lambda function
    square = lambda x: x ** 2

    print("==============================")
    print("       STUDENT REPORT")
    print("==============================")
    print()

    print(f"Name       : {name}")
    print(f"Course     : {course}")
    print(f"Marks      : {list(marks)}")
    print()

    print(f"Total      : {total}")
    print(f"Average    : {average}")
    print(f"Highest    : {highest}")
    print(f"Lowest     : {lowest}")
    print(f"Grade      : {grade}")
    print(f"Square of highest mark : {square(highest)}")


# Function call
student_report(
    "Hariharan",
    85,
    72,
    91,
    68,
    79
)