paragraph = input("Enter a paragraph: ")
n_sentence = 0

for i in range(len(paragraph)):
    if paragraph[i] in ['.', '!', '?']:
        
        if i == len(paragraph) - 1:
            n_sentence += 1
            
        elif paragraph[i + 1] not in ['.', '!', '?']:
            n_sentence += 1

print("Number of sentences is: ", n_sentence)