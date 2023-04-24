def Nhap():
    n=int(input("n="))
    return n
def Kiemtra(x):
    for i in range(2,x):
        if x%i==0: return False
        else: return True
def SNT(n):
    i=1
    x=2
    while i<=n:
        if Kiemtra(x):
            print(x,end=", ")
            i+=1
        x=x+1       
n=Nhap()
SNT(n)
            
        
        
