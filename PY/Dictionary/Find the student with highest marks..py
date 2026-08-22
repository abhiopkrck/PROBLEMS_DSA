students = [
    {"name": "Abhi", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Amit", "marks": 91},
    {"name": "Rohan", "marks": 48}
]

higest=0
higest_name=None

for student in students:
    if student["marks"]>higest:
        higest=student["marks"]
        higest_name=student["name"]
print(higest)
print(higest_name)
