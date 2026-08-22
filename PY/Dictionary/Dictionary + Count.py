students = {
    "Abhi": 85,
    "Rahul": 72,
    "Amit": 91,
    "Rohan": 68,
    "Raj": 55
}
count=0
for name,marks in students.items():
    if marks>=60:
        count+=1

print(count)