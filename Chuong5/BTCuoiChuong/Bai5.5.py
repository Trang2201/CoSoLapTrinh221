def Nhap():
    n=int(input("n="))
    A=[]
    for i in range(n):
        a=int(input())
        A.append(a)
    return A
def Tong(A):
    s=0
    for i in range(len(A)):
        if i%2!=0:
            s=s+A[i]
    return s
A=Nhap()
s=Tong(A)
print("Tong=" + str(s))