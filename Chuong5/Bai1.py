x=int(input())
k=int(input())
n=int(input())
L=[]
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
def add(L,x,k):
    if k>len(L): L=L+[x]
    else: L.insert(k,x)
    return L
def Inkq(L):
    print(L)

L=add(L,x,k)
Inkq(L)
