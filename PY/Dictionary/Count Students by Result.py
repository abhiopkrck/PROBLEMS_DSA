students = [
    {"name": "Abhi", "marks": [80, 85, 90]},
    {"name": "Rahul", "marks": [70, 75, 80]},
    {"name": "Amit", "marks": [90, 95, 92]},
    {"name": "Rohan", "marks": [40, 50, 45]},
    {"name": "Raj", "marks": [55, 60, 50]}
]

def calculate_avg(student):
    
    total=0
    for mark in student["marks"]:
        total +=mark
    avg=total/len(student["marks"])
    return avg

pass_student=0
Fail_student=0
for student in students:
    avg=calculate_avg(student)
    if avg>=60:
        pass_student+=1
    else:
        Fail_student+=1
print(f"pass:{pass_student}")
print(f"Fail:{Fail_student}")