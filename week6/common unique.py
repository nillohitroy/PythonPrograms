set1 = set()
set2 = set()

n1 = int(input("Enter number of elements: "))
for i in range(n1):
    ele = int(input("Enter an element: "))
    set1.add(ele)
    
n2 = int(input("Enter number of elements: "))
for i in range(n2):
    ele = int(input("Enter an element: "))
    set2.add(ele)
    
intersection = set1.intersection(set2)
inter_sum = sum(intersection)
print("Common: ", intersection, " Sum: ", inter_sum)

unique = set1.symmetric_difference(set2)
unique_sum = sum(unique)
print("Unique: ", unique, " Sum: ",unique_sum)

sorted_list = sorted(list(set1.union(set2)))
print("Sorted List: ", sorted_list)