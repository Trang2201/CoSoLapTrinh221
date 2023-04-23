def Nhap():
    n=int(input())
    return n
def Xuly(n):
    if n<=1: return 'Khong hop le!'
    else: 
        i=n+1
        while i>n:
            for j in range(2,i):
                if i%j==0: i=i+1
            return i
def Inkq(kq):
    print(kq)
n=Nhap()
kq=Xuly(n)
Inkq(kq)
            