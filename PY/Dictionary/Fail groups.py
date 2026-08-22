students = {
    "Abhi": 85,
    "Rahul": 72,
    "Amit": 91,
    "Rohan": 48,
    "Raj": 55
}

passs=[]
fail=[]

higest=0
higest_name=None
lowest=students["Abhi"]
lowest_name=None

for name,marks in students.items():
    
    if marks>higest:
        higest=marks
        higest_name=name
        
    if marks<lowest:
        lowest=marks
        lowest_name=name
        
    if marks>=60:
        passs.append(name)
    else:
        fail.append(name)

print("pass",passs)
print("Fail",fail)
print(f"Higest:{higest} Higest_student:{higest_name}")
print(f"Lowest:{lowest} Lowest_Student:{lowest_name}")