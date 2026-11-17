"""
Student Grade Calculator
Week 2 Python Project: Decisions, Loops, Functions, and Error Handling

Grading scale:
A: 90-100 | B: 80-89 | C: 70-79 | D: 60-69 | F: 0-59
"""

def get_grade(marks):
    """Return the grade for a valid mark (0 to 100)."""
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def get_message(grade):
    """Return an encouraging message for each grade."""
    messages = {
        "A": "Excellent work! You are doing amazing. Keep shining! 🌟",
        "B": "Very Good! Keep it up! 👍",
        "C": "Good effort! Keep practising and you will improve. 😊",
        "D": "You passed! Work a little harder to achieve more. 💪",
        "F": "Do not give up! Learn from mistakes and try again. ❤️",
    }
    return messages[grade]


def get_valid_marks():
    """Keep asking until the user enters a number from 0 through 100."""
    while True:
        raw_marks = input("Enter marks (0-100): ").strip()
        try:
            marks = float(raw_marks)
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks! Please enter a value from 0 to 100.")
        except ValueError:
            print("Invalid input! Please enter a number, such as 85 or 72.5.")


def main():
    print("=" * 42)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 42)

    name = input("Enter student name: ").strip()
    while not name:
        print("Name cannot be empty. Please try again.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade = get_grade(marks)
    message = get_message(grade)

    print("\n" + "=" * 42)
    print(f"          RESULT FOR {name.upper()}")
    print("=" * 42)
    print(f"Marks : {marks:g}/100")
    print(f"Grade : {grade}")
    print(f"Message: {message}")
    print("=" * 42)


if __name__ == "__main__":
    main()
