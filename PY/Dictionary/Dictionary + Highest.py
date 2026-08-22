students = {
    "Abhi": 85,
    "Rahul": 72,
    "Amit": 91,
    "Rohan": 68
}

higest=0
higest_name=None

for name,marks in students.items():
    if marks>higest:
        higest=marks
        higest_name=name
print(higest_name)
print(higest)