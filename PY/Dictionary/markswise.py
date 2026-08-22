students = {
    "Abhi": 85,
    "Rahul": 72,
    "Amit": 91,
    "Rohan": 68
}

for name ,marks in students.items():
    if marks>80:
        print(f"Name:{name} Marks:{marks}")