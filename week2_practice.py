"""
Week 2 hands-on practice programs.
Run this file and choose an exercise from the menu.
"""

from datetime import datetime


def time_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        print("Good morning!")
    elif 12 <= hour < 17:
        print("Good afternoon!")
    elif 17 <= hour < 21:
        print("Good evening!")
    else:
        print("Good night!")


def number_guessing_game():
    secret = 7
    print("Guess the secret number (1-10).")
    while True:
        try:
            guess = int(input("Your guess: "))
            if guess == secret:
                print("Correct! You guessed it.")
                break
            elif guess < secret:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Please enter a whole number.")


def print_numbers():
    for number in range(1, 101):
        print(number, end=" ")
    print()


def rectangle_area(length, width):
    return length * width


def calculator():
    try:
        first = float(input("First number: "))
        operator = input("Choose +, -, *, /: ").strip()
        second = float(input("Second number: "))
        if operator == "+":
            answer = first + second
        elif operator == "-":
            answer = first - second
        elif operator == "*":
            answer = first * second
        elif operator == "/":
            if second == 0:
                print("Cannot divide by zero.")
                return
            answer = first / second
        else:
            print("Unknown operator.")
            return
        print("Answer:", answer)
    except ValueError:
        print("Please enter valid numbers.")


def grading_scenario():
    try:
        marks = float(input("Enter marks (0-100): "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
        elif marks >= 90:
            print("Grade A")
        elif marks >= 80:
            print("Grade B")
        elif marks >= 70:
            print("Grade C")
        elif marks >= 60:
            print("Grade D")
        else:
            print("Grade F")
    except ValueError:
        print("Please enter a number.")


def age_category():
    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age < 13:
            print("Child")
        elif age < 20:
            print("Teenager")
        elif age < 60:
            print("Adult")
        else:
            print("Senior")
    except ValueError:
        print("Please enter a whole number.")


def main():
    exercises = {
        "1": ("Time-of-day greeting", time_greeting),
        "2": ("Number guessing game", number_guessing_game),
        "3": ("Print numbers 1 to 100", print_numbers),
        "4": ("Rectangle area function", lambda: print(
            "Area:", rectangle_area(
                float(input("Length: ")), float(input("Width: "))
            )
        )),
        "5": ("Simple calculator", calculator),
        "6": ("Grading scenario", grading_scenario),
        "7": ("Age category", age_category),
    }
    while True:
        print("\\nWEEK 2 PRACTICE MENU")
        for key, (label, _) in exercises.items():
            print(f"{key}. {label}")
        print("0. Exit")
        choice = input("Choose an exercise: ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        selected = exercises.get(choice)
        if selected:
            try:
                selected[1]()
            except ValueError:
                print("Please enter valid numeric values.")
        else:
            print("Invalid menu choice.")


if __name__ == "__main__":
    main()
