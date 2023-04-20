x=int(input("x="))
k=int(input("k="))
n=int(input("n="))
L=[]
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
def add(L,x,k):
    L=L[:(k)] + [x] + L[(k):]
    return L
L=add(L,x,k)
print(L)

