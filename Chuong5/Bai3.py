x=int(input())
n=int(input())
L=[]
for i in range(1,n+1):
    a=int(input())
    L.append(a)
def delete(L,x):
    while x in L:
        L.remove(x)
    return L
def Inkq(L):
    print(L)
L=delete(L,x)
Inkq(L)