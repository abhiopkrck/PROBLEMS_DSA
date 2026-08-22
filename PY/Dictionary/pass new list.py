students = [
    {"name": "Abhi", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Amit", "marks": 91},
    {"name": "Rohan", "marks": 48},
    {"name": "Raj", "marks": 55}
]

passed_students =[]

for student in students:
    if student["marks"]>=60:
        passed_students .append(student)

print(passed_students )