
d={'a':4,'b':2,'c':7,'d':3}
l=list(d.values())
print(l)
l1=[]
for i in range(len(l)):
    min=l[0]
    for x in l:
        if(x<min):
            min=x

    l1.append(min)
    l.remove(min)
print(l1)
i=0
d1={}
for i in l1:
    for key,val in d.items():
        if(i==val):
            d1[key]=val
            
print(d1)
        
