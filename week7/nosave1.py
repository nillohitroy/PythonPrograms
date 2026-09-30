mydict1={}
print("1 ",type(mydict1))
mydict = dict()
print("2 ",type(mydict))

mydict={"a":{1:"aaa",2:"abb",3:"acc"},"b":["abb","ccc"],"c":{"acc","caa"},"d":("daa","dbb")}

print("3 ",mydict)
print("4 ",mydict.items())
print("5 ",mydict.values())
print("6 ",mydict.keys())
for i in mydict.keys():
    print( "   7 ",mydict[i],"  ",type(mydict[i]))

for i in mydict.items():
    print("    7a ",i)
    
    
for i in mydict.keys():
    print("    8 ",i)

for i in mydict:
    print("    8a ",i)
    
#get() value with key
a=mydict.get("a")

print("9 ",a)

print("10 ",mydict["b"])
