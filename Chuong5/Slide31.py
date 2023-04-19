a=[]
for i in range(1,11):
    n=int(input())
    a=a+[n]              #a.append(n)
x=int(input("x="))

def Thaythe(x,a):
    for i in range(len(a)):
        if a[i]==5: a[i]=x
    for i in a:
        print(i,end=", ")
    return a
    
def Xoa(x,a1):
    i=0
    while i<len(a1):                       
        if a1[i]==x: del(a1[i])            
        else: i=i+1 
    for i in a1: print(i,end=", ")      # while x in a1:
                                        #     a1.remove(x)
                                        # for i in a1: print(i,end=", ")
    
print("Cau a:")   
a1=Thaythe(x,a)
print()
print("Cau b:")
Xoa(x,a1)






        