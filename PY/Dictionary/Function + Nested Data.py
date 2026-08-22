students = [
    {"name": "Abhi", "marks": [80, 85, 90]},
    {"name": "Rahul", "marks": [70, 75, 80]},
    {"name": "Amit", "marks": [90, 95, 92]},
    {"name": "Rohan", "marks": [40, 50, 45]}
]

def calculate_avg(student):
    total=0
    higest=0
    for mark in student["marks"]:
        total+=mark
    avg=total/len(student["marks"])
    return avg

highest_name = None
higest=0

for student in students:
    avg=calculate_avg(student)
    if avg>higest:
        higest=avg
        highest_name=student["name"]
print(f"{student['name']}:{higest}")