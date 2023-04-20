def Nhap():
    L=[]
    n=int(input("n="))
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def delete(L):
    i=0
    while i<len(L):
        j=i+1
        while j<len(L):
            if L[i]==L[j]: del(L[j])
            else: j=j+1
        i=i+1
    M=L.copy()
    return M
L=Nhap()
M=delete(L)
for i in M: print(i,end=" ")