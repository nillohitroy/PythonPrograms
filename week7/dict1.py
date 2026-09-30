# Create a dictionary of 5 students with name , three
# subjects (Physics, Chemistry and Mathematics) and number (
# out of 100 ) against each subject

dict1 = {"Names": [], "Subjects": ["Physics", "Chemistry", "Mathematics"], "Marks": []}
names = []
marks = []

for _ in range(5):
    n = input("Enter name: ")
    scores = []
    for _ in range(3):
        m = int(input("Enter marks: "))
        scores.append(m)
    names.append(n)
    marks.append(scores)
    
dict1['Names'] = names
dict1['Marks'] = marks

# Total
for i in range(5):
    total = list(sum(dict1["Marks"][i]))
    print(f"Total for {dict1["Names"][i]}: ", total[i])

# Highest Total & Individual
max_total = max(total.values())
max_name = [name for name, tot in total if tot == max_total]

print("Highest total mark students: ")
for i in max_name:
    print(i, " ", max_total)

h_p = max(dict1.items(), key=lambda x: x["Marks"][0])
h_c = max(dict1.items(), key=lambda x: x["Marks"][1])
h_m = max(dict1.items(), key=lambda x: x["Marks"][2])

print(h_p, h_c, h_m)
