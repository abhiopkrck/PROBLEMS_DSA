students = {
    "Abhi": 85,
    "Rahul": 72,
    "Amit": 91,
    "Rohan": 68
}

total=0
avg=0

for name,marks in students.items():
    total=total+marks

avg=total/4
print(total)
print(avg)