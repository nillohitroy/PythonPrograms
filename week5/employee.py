employees = []
print("Enter data for 5 employees: ")

for i in range(5):
    print(f"Employee {i+1}: ")
    place = input("Office Place: ")
    name = input("Name: ")
    emp_id = input("E_ID_No: ")
    basic = int(input("Enter basic Salary: "))
    hra = int(input("Enter HRA: "))
    
    da = 1.25 * basic
    
    gross = basic + hra + da
    
    employees.append([emp_id, name, place, basic, hra, da, gross])
    
n = len(employees)
for i in range(n):
    for j in range(0, n-i-1):
        if employees[j][0] > employees[j+1][0]:
            employees[j], employees[j+1] = employees[j+1], employees[j]
            
print("Sorted Order: ")
for emp in employees:
    print(f"Employee ID: {emp[0]}\nName: {emp[1]}\nPlace: {emp[2]}\nBasic: {emp[3]}\nHRA: {emp[4]}\nDA: {emp[5]}\nGross: {emp[6]}")