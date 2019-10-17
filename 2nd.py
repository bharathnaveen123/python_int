
def max(l):
    n=len(l)
    ca=cm=cr=0
    for i in range(n):
        if(l[i]=='A'):
           ca+=1
        elif(l[i]=='M'):
           cm+=1
        elif(l[i]=='R'):
           cr+=1
        else:
           pass
        
    if(ca>cm and ca>cr):
           return "Artificial Intelligence"
    elif(cm>ca and cm>cr):
           return "Machine Learning"
    else:
           return "Robotics"

n=int(input("n:  "))
l=[]
for i in range(n):
    id1=int(input("id  :"))
    c=input("course  :")
    c=c.upper()
    l.append(id1)
    l.append(c)
    
print(l)
print(max(l))
