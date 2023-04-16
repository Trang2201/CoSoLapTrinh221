def Nhap():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def Trungbinh(a,b,c):
    if b<=a<=c or c<=a<=b: median=a
    elif a<=b<=c or c<=b<=a: median=b
    else: median=c
    return median
def Inkq(median):
    print("So trung binh la:",median)
a,b,c=Nhap()
median=Trungbinh(a,b,c)
Inkq(median)        