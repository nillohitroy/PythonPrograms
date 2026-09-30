x={'a':[1,2,3],'b':[4,5,6],'c':['x',1,[8.9]]}
print(" 1",x)

x['b']=['''changed
 value''']

print(" 2",x)
print(" 3",x['b'][0])
print(" 4",x['b'][0][3])
print(" 5",x['b'][0][1:11:2])