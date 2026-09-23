paragraph = input("Enter a paragraph: ")


sentences = []
for s in paragraph.split('.'):
    if s.strip():
        sentences.append(s.strip())
       
sentence_lists = []
for sentence in sentences:
    sentence_lists.append(sentence.split())
    
for i in range(len(sentence_lists)):
    count = len(sentence_lists[i])
    print(f"Sentence {i+1} has {count} words.")
    
if len(sentence_lists) >= 2:
    reverse = []
    for i in range(len(sentence_lists[1]) - 1, -1, -1):
        reverse.append(sentence_lists[1][i])
    sentence_lists[1] = reverse
    
final = ""
for s in sentence_lists:
    final += " ".join(s) + ". " 
    
print("Paragraph:", final.strip())
