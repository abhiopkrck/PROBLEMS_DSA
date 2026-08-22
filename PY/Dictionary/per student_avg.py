students = [
    {"name": "Abhi", "marks": [80, 85, 90]},
    {"name": "Rahul", "marks": [70, 75, 80]},
    {"name": "Amit", "marks": [90, 95, 92]},
    {"name": "Rohan", "marks": [40, 50, 45]}
]   

student_1 = {"name": "Abhi", "marks": [80, 85, 90]}

for student in students:
    total=0

    for mark in student["marks"]:
        total+=mark

    avg=total/len(student["marks"])

    print(f"{student["name"]}:{avg}")