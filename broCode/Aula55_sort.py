students = ["Squidward", "Sandy", "Patrick", "Zar", "SpongeBob", "Mr.Krabs"]
print(sorted(students))

students.sort(reverse=True)
for i in students:
    print(i, end=" ")
print()

students_data = [
    ("Squidward", 90),
    ("Sandy", 38),
    ("Patrick", 6),
    ("SpongeBob", 77),
    ("Mr.Krabs", 65)
]

students_data.sort()
for i in students_data:
    print(i, end=" ")
print()

grade = lambda grades: grades[1]
students_data.sort(key=grade, reverse=True)
for i in students_data:
    print(i, end=" ")
print()

students_data_sorted = sorted(students_data, key=grade)

print(students_data_sorted)