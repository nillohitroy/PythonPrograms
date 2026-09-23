n = int(input("Enter the number of elements: "))
lists = []
for i in range(n):
    ele = int(input("Enter an element: "))
    lists.append(ele)
    
# Insertion sort
for i in range(1, n):
    key = lists[i]
    j = i - 1
    while j >= 0 and key < lists[j]:
        lists[j+1] = lists[j]
        j -= 1
    lists[j+1] = key
    
print("Sorted List: ", lists)

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
list2 = list([num1, num2])

for num in list2:
    pos = 0
    while pos < len(lists) and lists[pos] < num:
        pos += 1
    lists.insert(pos, num)
    
print("New list: ",lists)