students = {
    "Abhi": 85,
    "Rahul": 72,
    "Amit": 91,
    "Rohan": 48,
    "Raj": 55,
    "Akash": 78
}

result={}

for name,marks in students.items():
    if marks>=60:
        result[name]="pass"
    else:
        result[name]="fail"
        
print(result)