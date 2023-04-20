def Nhap():
    A=[]
    for i in range(10):
        n=int(input())
        A.append(n)
    return A
def HoanDoi(A):
    B=A.copy()
    for i in range(0,len(A),2):
        B[i]=A[i+1]
        B[i+1]=A[i]
    return B
A=Nhap()
B=HoanDoi(A)
for i in B: print(i,end=" ")