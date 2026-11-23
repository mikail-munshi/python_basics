# Python Fundamentals Practice

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05033?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-121011?style=for-the-badge&logo=github&logoColor=white)

A beginner-friendly collection of notes and practice code built while learning the fundamentals of **Python**, after exploring C, C++, Java, and JavaScript. Each topic is organized into parts, with inline comments explaining the concept and small practice exercises. More topics will be added as the learning journey continues.

## Topics Covered

### Part 1: Basics
* **Output (`print`)**: Printing text and variables, and how multiple arguments are automatically separated by a space.
* **Variables & Data Types**: Creating variables and checking their types with `type()` (`str`, `int`).
* **User Input (`input`)**: Reading data from the user and greeting them using both comma-separated printing and string concatenation (`+`).

### Part 2: Type Casting & Strings
* **Type Casting vs Type Conversion**: Explicit casting (`int()`, `float()`) versus implicit conversion done automatically by Python (`1 + 2.5`).
* **Input Pitfalls**: Why `input()` always returns a string (`"2" + "3"` gives `"23"`) and how to fix it with `int(input())`.
* **String Operations**: `upper()`, `find()` (0-based index, returns `-1` if not found), `replace()` (strings are immutable, so the result must be stored or printed), and presence checks with the `in` keyword.
* **Reserved Keywords**: Words such as `in`, `True`, `while`, `break`, and `for` that cannot be used as variable names.
* **Practice Exercises**: Calculating the total and average of three prices, and checking whether a superhero name starts with "S".

### Part 3: Operators & Conditionals
* **Arithmetic Operators**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulus), and `**` (power).
* **Assignment Operators**: `=`, `+=`, `-=`, `*=`, `/=`.
* **Operator Precedence**: How `()`, `*`, `/`, `+`, `-` are evaluated, similar to BODMAS in math.
* **Comparison Operators**: `<`, `>`, `==`, `!=`, returning `True` or `False`.
* **Logical Operators**: `and`, `or`, `not`.
* **Conditional Statements**: Decision making with `if` / `else` using a voting-age example.

## Project Structure

```text
python_basics/
├── code.py                 # Practice code & notes for all parts
└── README.md               # Project documentation
```


## Learnings

Building this project provided hands-on experience with:

* Writing and running basic Python programs using `print()` and `input()`.
* Understanding dynamic typing and checking types with `type()`.
* Converting between data types using type casting and recognizing implicit type conversion.
* Manipulating strings with built-in methods and understanding string immutability.
* Using arithmetic, assignment, comparison, and logical operators, along with operator precedence.
* Controlling program flow with `if` / `else` conditional statements and Python's indentation rules.

## Upcoming Topics

* More conditionals (`elif`) and loops (`for`, `while`)
* Data structures (lists, tuples, sets, dictionaries)
* Functions
* File handling and more