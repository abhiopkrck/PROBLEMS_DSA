students = (
    ("Abhi", 80),
    ("Rahul", 65),
    ("Amit", 92),
    ("Rohan", 75)
)

def highest_marks(students):
    higest=0
    higest_name=None

    for name,marks in students:
        if marks>higest:
            higest=marks
            higest_name=name

    return higest,higest_name




higest_name,higest=highest_marks(students)

print(higest_name)
print(higest)