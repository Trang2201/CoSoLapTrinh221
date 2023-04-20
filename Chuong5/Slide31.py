a=[]
for i in range(10):
    n=int(input())
    a.append(n)
x=int(input("x="))

def Thaythe(x,a):
    for i in range(len(a)):
        if a[i]==5: a[i]=x
    Inkq(a)
    return a

def Xoa(x,a):
    i=0
    while i<len(a):                       
        if a[i]==x: del(a[i])            
        else: i=i+1 
    Inkq(a)
    
def Inkq(a):
    for i in a:
        print(i,end=", ")
    print()
        
a=Thaythe(x,a)
Xoa(x,a)
    







        