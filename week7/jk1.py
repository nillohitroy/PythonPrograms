students = {}
for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    physics = float(input(f"Enter the marks of {name} in Physics: "))
    chemistry = float(input(f"Enter the marks of {name} in Chemistry: "))
    mathematics = float(input(f"Enter the marks of {name} in Mathematics: "))
    students[name] = {"Physics": physics, "Chemistry": chemistry, "Mathematics": mathematics}

print(students)

# Calculating total marks for each student
for name, marks in students.items():
    total = sum(marks.values())
    students[name]["Total"] = total

# Finding highest and second highest in individual subjects
highest_physics = max(students.items(), key=lambda x: x[1]["Physics"])

highest_chemistry = max(students.items(), key=lambda x: x[1]["Chemistry"])

highest_mathematics = max(students.items(), key=lambda x: x[1]["Mathematics"])

second_highest_physics = sorted(students.items(), key=lambda x: x[1]["Physics"], reverse=True)[1]

second_highest_chemistry = sorted(students.items(), key=lambda x: x[1]["Chemistry"], reverse=True)[1]

second_highest_mathematics = sorted(students.items(), key=lambda x: x[1]["Mathematics"], reverse=True)[1]

# Finding students with more than 60% in Physics but less than 70% in Chemistry
students_physics_chemistry = [name for name, marks in students.items() if marks["Physics"] > 60 and marks["Chemistry"] < 70]

# Displaying the results in a tabular format
print("\nStudent Marks Table:")
print("-" * 60)
print(f"{'Name':<15} {'Physics':<10} {'Chemistry':<10} {'Mathematics':<10} {'Total':<10}")
print("-" * 60)
for name, marks in students.items():
    print(f"{name:<15} {marks['Physics']:<10.2f} {marks['Chemistry']:<10.2f} {marks['Mathematics']:<10.2f} {marks['Total']:<10.2f}")
print("-" * 60)

print(f"\nHighest in Physics: {highest_physics[0]} with {highest_physics[1]['Physics']} marks")
print(f"Highest in Chemistry: {highest_chemistry[0]} with {highest_chemistry[1]['Chemistry']} marks")
print(f"Highest in Mathematics: {highest_mathematics[0]} with {highest_mathematics[1]['Mathematics']} marks")
print(f"\nSecond Highest in Physics: {second_highest_physics[0]} with {second_highest_physics[1]['Physics']} marks")
print(f"Second Highest in Chemistry: {second_highest_chemistry[0]} with {second_highest_chemistry[1]['Chemistry']} marks")
print(f"Second Highest in Mathematics: {second_highest_mathematics[0]} with {second_highest_mathematics[1]['Mathematics']} marks")
print(f"\nStudents with more than 60% in Physics but less than 70% in Chemistry: {', '.join(students_physics_chemistry)}")
