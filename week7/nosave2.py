k=1,2,3,4

v=7,8,9,10

i=dict.fromkeys(k,v)

print(" 1>> ",i)

i.update({5:"hello"})

print(" 2>> ",i)

i[3]="aaa"
print(" 3>> ",i)

a={x:x+2 for x in range(1,10)}

print(" 4>> ",a)

a={x:x+2 for x in range(1,10) if x>=4}

print(" 5>> ",a)

a={(1,2,3,4):[5,6],(7,8,9,10):[11,12]}

print(" 6>> ",a)

for i in a:
    for x in i:
      print("      7>> ",x,i)

for i in a.values():
    for x in i:
      print("      8>> ",x,i)      