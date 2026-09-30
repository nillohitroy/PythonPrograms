x={}
#creating items
for i in range(2):
    #adding keys
    a=input("outer loop "+str(i+1)+" : ")
    l=[]
    
    #adding values    
    for j in range(3):
        b=input("inner ")
        l.append(b)
    x.update({a:l})
    
l=set(x.keys())
k=list(x.values())
print("dict","  ",x)
print(l)
print(k)
print(x["1"][1])