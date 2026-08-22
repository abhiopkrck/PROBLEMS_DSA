students = [
    {"name": "Abhi", "marks": 85},
    {"name": "Rahul", "marks": 72},
    {"name": "Amit", "marks": 91},
    {"name": "Rohan", "marks": 48},
    {"name": "Raj", "marks": 55}
]

pass_student=[]
total=0
for student in students:
    if student["marks"]>=60:
        pass_student.append(student)
        total=total+student["marks"]
avg=total/len(pass_student)

print(avg)