def Nhap():
    s=input()
    a=int(input())
    return s,a
def center(s,a):
    n=len(s)
    khoangcach=" " * int((a-n)/2)
    if a<n: print(s)
    else: 
        s= khoangcach + s
        print(s)
s,a=Nhap()
center(s,a)

    