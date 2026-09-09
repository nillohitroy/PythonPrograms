paragraph = input("Enter a paragraph: ")
c_para = paragraph.replace("!", ".").replace("?", ".")

while '..' in c_para:
    c_para = c_para.replace("..", ".")

raw_sentence = c_para.split(".")

sentence = []
for i in raw_sentence:
    cleaned = i.strip()
    
    if cleaned != "":
        sentence.append(cleaned)

print(sentence)
if len(sentence) >= 3:
    s2 = sentence[1].split()
    s3 = sentence[2].split()
    
    part1 = s2[1][0:3]
    part2 = s3[0][2:5]
    print("\n", part1,"\n", part2)
    print("Concatenated String: ", part1 + part2)

        
else:
    print("Not enough sentences")