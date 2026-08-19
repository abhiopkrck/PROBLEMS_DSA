students = {
    "Abhi": 80,
    "Rahul": 65,
    "Amit": 92,
    "Rohan": 75
}
def highest_marks(students):
    higest = 0
    higest_student_name = None
    for name, marks in students.items():
        if marks > higest:
            higest = marks
            higest_student_name = name
    return higest_student_name, higest


higest_student_name,higest=highest_marks(students)
print("Student NAme Who Has Higest MArks:",higest_student_name)
print("Marks",higest)