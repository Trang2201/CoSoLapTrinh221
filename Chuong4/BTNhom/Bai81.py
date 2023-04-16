def Nhap():
    a=int(input("Nhap canh goc vuong thu nhat:"))
    b=int(input("Nhap canh goc vuong thu hai:"))
    return a,b
def Canhhuyen(a,b):
    import math
    c=math.sqrt(a*a+b*b)
    return c
def Inkq(c):
    print("Chieu dai canh huyen tam giac vuong=",c,sep="")
a,b=Nhap()
c=Canhhuyen(a,b)
Inkq(c)

    