sentence = input("Enter a sentence: ")
word = sentence.split()

if len(word) < 6:
    print("Enter words more than 6")
    
alt_tuple = tuple(word[::2])
print("Tuple with alternate words: ", alt_tuple)