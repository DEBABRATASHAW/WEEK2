# Week 2 Python Project — Student Grade Calculator

## 1. Project overview
The Student Grade Calculator accepts a student's name and marks, validates the marks, assigns a grade, and displays an encouraging message. It demonstrates decision-making, loops, functions, comparison operators, and basic exception handling.

## 2. Grading rules

| Marks | Grade | Message |
|---:|:---:|---|
| 90–100 | A | Excellent work! You are doing amazing. Keep shining! |
| 80–89.99 | B | Very Good! Keep it up! |
| 70–79.99 | C | Good effort! Keep practising and you will improve. |
| 60–69.99 | D | You passed! Work a little harder to achieve more. |
| 0–59.99 | F | Do not give up! Learn from mistakes and try again. |

The code accepts decimal marks too. For example, 89.5 receives grade B.

## 3. Files and folder structure

```text
week2_python_student_grade_calculator/
├── README.md
├── grade_calculator.py
├── week2_practice.py
├── test_cases.txt
└── screenshots/
    ├── sample_output.png
    └── invalid_input.png
```

- `grade_calculator.py`: final project.
- `week2_practice.py`: the seven hands-on practice exercises.
- `test_cases.txt`: manual test plan and expected results.
- `screenshots/`: sample terminal-output evidence.

## 4. Requirements
- Python 3.8 or newer.
- No third-party packages are required.

Check Python installation:

```bash
python --version
```

If that command is not recognized on Windows, try:

```powershell
py --version
```

## 5. Setup and run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the VS Code terminal (`Terminal` → `New Terminal`).
4. Run the final project:

```powershell
python grade_calculator.py
```

On Windows, if needed:

```powershell
py grade_calculator.py
```

To run the hands-on exercises:

```powershell
python week2_practice.py
```

## 6. How the program works

1. `main()` displays the title and asks for the student's name.
2. A `while` loop keeps asking if the name is empty.
3. `get_valid_marks()` repeatedly asks for marks until the input is numeric and between 0 and 100.
4. `try/except ValueError` prevents the program from crashing when non-numeric text is entered.
5. `get_grade(marks)` uses `if-elif-else` to select the grade.
6. `get_message(grade)` returns the matching encouragement.
7. The result is printed in a readable format.

### Functions used
- `main()`: controls the complete program.
- `get_valid_marks()`: validates input using a `while` loop and exception handling.
- `get_grade(marks)`: converts marks into a grade.
- `get_message(grade)`: returns a message for the grade.

### Concepts demonstrated
- **Conditionals:** `if`, `elif`, and `else` choose a grade.
- **Comparison operators:** `>=`, `<=`, and range checks compare values.
- **While loops:** repeat until valid input is received.
- **Functions:** keep the program modular and reusable.
- **Dictionary:** maps each grade to its message.
- **Exception handling:** catches invalid numeric input using `try/except`.

## 7. Algorithm

```text
START
  Ask for student name until it is not empty
  REPEAT
      Ask for marks
      If input is not numeric, show an error
      Else if marks are outside 0–100, show an error
  UNTIL marks are valid
  If marks >= 90, grade = A
  Else if marks >= 80, grade = B
  Else if marks >= 70, grade = C
  Else if marks >= 60, grade = D
  Else, grade = F
  Find the encouraging message for the grade
  Display name, marks, grade, and message
END
```

## 8. Testing
Use the cases in `test_cases.txt`. The program should reject blank names, text instead of marks, and values below 0 or above 100. It should accept 0 and 100.

## 9. Sample output

```text
Enter student name: Priya
Enter marks (0-100): 85

RESULT FOR PRIYA:
Marks : 85/100
Grade : B
Message: Very Good! Keep it up!
```

The screenshots folder contains illustrative terminal-style evidence. Run the program on your own computer and replace/add screenshots if your instructor requires screenshots captured from your actual run.

## 10. GitHub submission

Create a new public repository, for example `week2-python-grade-calculator`, then upload the files while keeping the folder structure.

Using Git from the project folder:

```bash
git init
git add .
git commit -m "Complete Week 2 Python Student Grade Calculator"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/week2-python-grade-calculator.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. Do not upload virtual environments or unrelated files.
