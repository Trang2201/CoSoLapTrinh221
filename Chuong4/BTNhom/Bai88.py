def Nhap():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def Kiemtra(a,b,c):
    if abs(b-c)<a<b+c: return True
    else: return False
def Inkq(kq):
    print(kq)
a,b,c=Nhap()
kq=Kiemtra(a,b,c)
Inkq(kq)