words = input("Enter a paragraph: ")

words = words.split()

punctuation = ".,!?:;'\"()"
ba_starts = 0
not_ba_ends = 0

for word in words:
    c_word = word.strip(punctuation)
    if c_word.casefold().startswith('BA'.casefold()):
        ba_starts += 1
    if not c_word.casefold().endswith("BA".casefold()):
        not_ba_ends += 1

print("Words starting with BA: ", ba_starts)
print("Words NOT ending with BA: ", not_ba_ends)