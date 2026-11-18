num_subjects = int(input("Enter number of subjects: "))
marks = []

for i in range(1, num_subjects + 1):
    score = float(input(f"Enter marks for Subject {i}: "))
    marks.append(score)

average = sum(marks) / num_subjects

if average >= 95:
    grade = "A+"
elif average >= 85:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 65:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Average: {average:.2f}")
print(f"Grade: {grade}")