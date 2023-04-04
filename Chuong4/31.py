def Nhap():
    n=int(input("n="))
    return n
def NhapVaDem(n):
    print("Nhap",n,"so nguyen:")
    kq=0
    for i in range(1,n+1):
        a=int(input())
        if (a%2==0)and(a!=0):
            kq=kq+1
    return kq
def InKQ(kq):
    print("So chu so chan la:",kq)
n=Nhap()
kq=NhapVaDem(n)
InKQ(kq)

        