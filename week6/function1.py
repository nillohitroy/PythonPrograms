tuple1 = (15, 25, 10, 30, 5)
tuple2 = (20, 30, 40)

print(max(tuple1, tuple2))
print(min(tuple1, tuple2))

def cmp(t1, t2):
    return (t1>t2) - (t1 < t2)

print(cmp(tuple1, tuple2))

del tuple1