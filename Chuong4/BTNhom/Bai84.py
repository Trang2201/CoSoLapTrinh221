def Nhap():
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def Trungbinh(a,b,c):
    max=a
    if max<b: max=b
    if max<c: max=c
    min=a
    if min>b: min=b
    if min>c: min=c
    median=a+b+c-min-max
    return median
def Inkq(median):
    print("So trung binh la:",median)
a,b,c=Nhap()
median=Trungbinh(a,b,c)
Inkq(median)