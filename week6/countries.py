inputs = input("Enter 10 countries: ").split()
    
all_countries = frozenset(inputs)

A = frozenset([inputs[0], inputs[1], inputs[3], inputs[4]])
B = frozenset([inputs[0], inputs[1], inputs[2], inputs[5]])
C = frozenset([inputs[0], inputs[2], inputs[6], inputs[7]])


print("i) Countries A has not visited:", all_countries - A)

print("ii) Countries A and B have visited together:", A & B)

print("iii) B and C visited but not A:", (B & C) - A)

print("iv) A, B, and C have visited:", A & B & C)

print("v) Unvisited by anyone:", all_countries - (A | B | C))

print("vi) Visited by C, but neither A nor B:", C - (A | B))
