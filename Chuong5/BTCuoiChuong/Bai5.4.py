def Nhap():
    n=int(input("n="))
    A=[]
    for i in range(n):
        a=int(input())
        A.append(a)
    return A
def DaoNguoc(A):
    A.reverse()
    B=A.copy()
    print(B)
    return B
def SapXep(B):
    B.sort()
    print(B)
A=Nhap()
B=DaoNguoc(A)
SapXep(B)