# 🐍 Python Logic Building — 100+ Problems Solved

> My Python logic-building practice journey
> **100+ problems solved** across Lists, Tuples, Dictionaries, Loops, Functions, Strings, Exception Handling and more.

---

## 📊 Progress

| Topic                       | Status         |
| --------------------------- | -------------- |
| Variables & Data Types      | ✅ Completed    |
| Input / Output              | ✅ Completed    |
| Conditions (`if/elif/else`) | ✅ Completed    |
| `while` Loops               | ✅ Completed    |
| `for` Loops                 | ✅ Completed    |
| Exception Handling          | ✅ Completed    |
| Lists                       | ✅ Completed    |
| Tuples                      | ✅ Completed    |
| Dictionaries                | ✅ Completed    |
| Functions                   | ✅ Completed    |
| Nested Data                 | ✅ Completed    |
| List + Dictionary Problems  | ✅ Completed    |
| String Problems             | 🚧 In Progress |
| LeetCode Problems           | 🚧 In Progress |

**Total Practice:** 🏆 **100+ Python problems**

---

# 📚 Problems Solved

## 1. 🔢 Basic Number & Logic Problems

* Find the smallest number in a collection
* Find the largest number in a collection
* Find smallest and largest together
* Calculate sum of numbers
* Calculate average of numbers
* Reverse an integer
* Check whether a number is palindrome
* Count digits
* Perform arithmetic operations
* Swap two variables
* Validate positive age
* Validate numeric input
* Handle division by zero

---

## 2. 🔁 Loops & Control Flow

* Basic `for` loop problems
* Basic `while` loop problems
* Infinite loop with `while True`
* Break loop after valid input
* Number validation using loops
* Password validation
* Password minimum length validation
* Password number validation
* Repeated user input handling
* Loop with `try/except`
* Loop with `else`
* Loop with `finally`

---

## 3. 🛡️ Exception Handling

Practiced:

```python
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
else:
    ...
finally:
    ...
```

Problems solved:

* Handle invalid integer input
* Handle division by zero
* Validate user input
* Retry invalid input using `while`
* Understand `else` in exception handling
* Understand `finally`
* Combine loops with exception handling

---

# 📋 4. Lists

Problems practiced:

* Find smallest element
* Find largest element
* Calculate total
* Calculate average
* Count repeated numbers
* Find most repeated number
* Find first unique number
* Separate even and odd numbers
* Filter numbers
* Append elements based on conditions
* Create result lists
* Work with nested lists
* Iterate through list elements

---

# 📦 5. Tuples

Problems practiced:

* Find smallest number in tuple
* Find largest number in tuple
* Find smallest and largest together
* Unpack tuple values
* Work with tuple of student records
* Find highest marks from tuple data
* Return multiple values from a function

Example:

```python
student = ("Abhi", 21, "Python")

name, age, skill = student
```

---

# 📖 6. Dictionaries

### Basic Dictionary Operations

* Access dictionary values
* Update dictionary values
* Add new dictionary keys
* Check whether a key exists
* Check dictionary values
* Loop through dictionary
* Use `.items()`
* Work with key/value pairs

### Dictionary Logic Problems

* Find highest marks
* Find lowest marks
* Find highest-mark student
* Find lowest-mark student
* Count passing students
* Separate pass/fail students
* Calculate total marks
* Calculate average marks
* Filter products by price
* Find most expensive product
* Create expensive products dictionary
* Create cheap products dictionary
* Apply discount to products
* Apply discount only to selected products
* Create Pass/Fail result dictionary
* Count frequency of numbers
* Find most repeated number
* Find unique numbers

---

# 🧩 7. Functions

Practiced:

* Create basic functions
* Function parameters
* Function return values
* Return multiple values
* Function with loops
* Function with conditions
* Function with lists
* Function with tuples
* Function with dictionaries
* Function with nested data

Examples practiced:

```python
def calculation(a, b):
    return a + b
```

```python
def analyze(numbers):
    ...
    return largest, smallest, average
```

```python
def highest_marks(students):
    ...
    return highest, highest_name
```

---

# 🏫 8. Student Data Problems

Worked extensively with student records.

Examples:

```python
students = {
    "Abhi": 85,
    "Rahul": 72,
    "Amit": 91
}
```

and:

```python
students = [
    {"name": "Abhi", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Amit", "marks": 91}
]
```

Problems solved:

* Print student information
* Find highest marks
* Find lowest marks
* Find highest-mark student
* Find lowest-mark student
* Count passing students
* Separate pass/fail students
* Calculate total marks
* Calculate average marks
* Filter passing students
* Store passing students in a new list
* Calculate average of passing students

---

# 🧠 9. Nested Data

Started working with:

```text
List
 ↓
Dictionary
 ↓
List
```

Example:

```python
students = [
    {
        "name": "Abhi",
        "marks": [80, 85, 90]
    }
]
```

Problems solved:

* Access nested dictionary data
* Access nested marks list
* Calculate marks average
* Calculate average for every student
* Find highest average
* Find student with highest average
* Count students based on average
* Combine functions with nested data
* Combine loops with nested data

---

# 🔥 10. Logic Patterns Learned

These patterns are becoming familiar:

### Counter

```python
count = 0

for item in items:
    count += 1
```

### Total

```python
total = 0

for num in numbers:
    total += num
```

### Highest

```python
highest = 0

for num in numbers:
    if num > highest:
        highest = num
```

### Highest + Name

```python
if marks > highest:
    highest = marks
    highest_name = name
```

### Filtering

```python
if marks >= 60:
    ...
```

### Dictionary `.items()`

```python
for name, marks in students.items():
    ...
```

### Nested Data

```python
for student in students:
    for mark in student["marks"]:
        ...
```

---

# 💻 11. LeetCode Practice

Started solving LeetCode-style problems.

### Palindrome Number

Problem:

> Given an integer `x`, return `True` if it is a palindrome.

Practiced:

```text
121 → True
-121 → False
10 → False
```

Also practiced integer reversal logic.

---

# 🚧 12. Currently Learning

## Strings

Next problems:

* Reverse a string
* Count characters
* Count vowels
* Count consonants
* Check string palindrome
* Find duplicate characters
* Find unique characters
* Character frequency
* Word frequency
* Reverse words

Current goal:

```text
Integer Logic
      ↓
List Logic
      ↓
Dictionary Logic
      ↓
Nested Data
      ↓
Functions
      ↓
String Logic
      ↓
LeetCode
```

---

# 🎯 Current Goal

The main goal is **not memorizing code**.

The goal is to understand:

```text
Problem
   ↓
Understand data
   ↓
Choose loop
   ↓
Choose condition
   ↓
Track result
   ↓
Return / Print result
```

I am focusing on improving **Python problem-solving and logical thinking** step by step.

---

# 📈 Learning Journey

### Phase 1 — Python Basics

✅ Variables
✅ Input/Output
✅ Conditions
✅ Loops

### Phase 2 — Core Data Structures

✅ Lists
✅ Tuples
✅ Dictionaries

### Phase 3 — Logic Building

✅ Counting
✅ Searching
✅ Filtering
✅ Maximum / Minimum
✅ Average
✅ Frequency
✅ Nested data

### Phase 4 — Functions

✅ Parameters
✅ Return values
✅ Multiple returns
✅ Functions + data structures
✅ Functions + nested data

### Phase 5 — Problem Solving

✅ LeetCode started
🚧 String problems
🚧 More medium-level problems

---

# 🏆 Achievement

## 100+ Python Logic Problems Solved 🎉

Started with basic:

```text
if / else
```

and progressed to:

```text
Lists
   ↓
Tuples
   ↓
Dictionaries
   ↓
Functions
   ↓
Nested Data
   ↓
LeetCode
```

The focus is now shifting from **learning syntax** to **building logic independently**.

---

## 🚀 Next Target

* [ ] Complete String Logic
* [ ] Solve more LeetCode Easy problems
* [ ] Improve problem-solving speed
* [ ] Start Medium-level problems
* [ ] Build Python mini-projects
* [ ] Apply Python logic to AI/ML projects

---

### ⭐ Progress: 100+ Problems Completed

**Keep solving. Keep debugging. Keep improving. 🚀**
