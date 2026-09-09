paragraph = input("Enter a paragraph: ")
splits = paragraph.split()

for i in range(len(splits)):
    if i % 2 == 0:
        splits[i] = "".join(reversed(splits[i]))

print("The output: ")
for i in splits:
    print(i, sep=" ", end=" ")