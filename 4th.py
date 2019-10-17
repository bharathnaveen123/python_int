class bill:
    def __init__(slef):
        bill_amount=0
        
    def calc(self,cfee,qlist,plist):
        total_bill_amount=0
        total_bill_amount+=cfee
        med=0
        for i in range(len(qlist)):
            med+=(qlist[i]*plist[i])
        total_bill_amount+=med
        self.bill_amount=total_bill_amount

        return total_bill_amount

b=bill()
q=[2,5]
p=[100,20]
id=int(input("id :"))
name=input("Name  :")
print("ID  :",id)
print("Name  :",name)

print("total bill amount :",b.calc(10,q,p))
