class RetailShop:
    def __init__(self):
        self.bname=" "
        self.dcat={}

    def get_book_name(self):
        self.bname=input("enter sub:")
        return self.bname
    def get_category_list(self):
        tot=int(input("no of books:"))
        sold=int(input("sold books:"))
        self.dcat[self.bname]=[tot,sold]
        return self.dcat
    def count_No_booksold(self):
        d={}
        d=self.dcat
        sum=0
        for val in d.values():
            sum+=val[1]

        return sum
    def check_stock(self):
        d={}
        d=self.dcat
        l=[]
        for key,val in d.items():
            tot=val[0]
            sold=val[1]
            per=.60*tot
            if(sold>per):
                l.append(key)
                l.append(tot-sold)

        return l
                
            
        

        
r=RetailShop()
n=int(input("enter no of category of books:   "))
for i in range(n):
    bname=r.get_book_name()
    print(bname)
    l={}
    l=r.get_category_list()

print(l)
s=r.count_No_booksold()
print("no of sold in shop   :",s)
print(r.check_stock())

    
        
