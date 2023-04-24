def Nhap():
    n=int(input("n="))
    return n
def Kiemtra(n):
    s=0
    for i in range(2,n):
        if n%i==0: s+=1
    return s
def Inkq(n,s):
    if s==0: print(n,"la SNT")
    else: print(n,"khong la SNT")
n=Nhap()
s=Kiemtra(n)
Inkq(n,s)