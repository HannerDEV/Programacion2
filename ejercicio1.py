students = [
    ("Ana", 20, "Python", 85),
    ("Carlos", 19, "Java", 72),
    ("Maria", 21, "Python", 95),
    ("Juan", 18, "Java", 60),
    ("Sofia", 20, "Python", 88),
]

subjects = ["Python", "Java", "Python", "Java", "Python"]

sorted_students = sorted(students, key=lambda student: student[3],
                          reverse=True)

for i, student in enumerate(sorted_students):
    print(f"Estudiante {i + 1}: {student[0]} Score: {student[3]}")

for student, language in zip(students, subjects):
    print(student[0], language)

higher_grades = [student for student in students if student[3] >= 80]

print(higher_grades)

subjects_noduplicated = set(subjects)

print(subjects_noduplicated)

dict_students = {student[0]: student[3] for student in students}

for student in students:
    try:
        assert student[3] > 0 and student[3] < 100, "Out of value"
    finally:
        print("good")

name = ""

grade = 0

try:
    name = input("enter student name: ")
    grade = dict_students[name]
    print(f"{name}'s grade: {grade}")
except KeyError:
    print("User not found")

sum = 0

for student in students:
    sum += student[3]

print(sum/len(students))
