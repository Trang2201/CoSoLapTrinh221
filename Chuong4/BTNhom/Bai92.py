def Nhap():
    n=int(input("n="))
    return n
def Kiemtra(n):
    if n<=1: return 'Khong hop le!'
    for i in range(2,n):
        if n%i==0: return False
    return True
def Inkq(kq):
    print(kq)
n=Nhap()
kq=Kiemtra(n)
Inkq(kq)