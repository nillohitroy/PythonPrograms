set1 = {1, 2, 3}
set2 = {4, 5, 6}

set1.add(99)
print("After adding: ", set1)

set3 = set1.copy()
print("Copied Set: ", set3)

isdisjoint = set1.isdisjoint(set2)
print(isdisjoint)