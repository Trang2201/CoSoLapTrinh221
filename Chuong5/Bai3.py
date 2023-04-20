x=int(input("x="))
n=int(input("n="))
L=[]
for i in range(1,n+1):
    a=int(input())
    L.append(a)
def delete(L,x):
    i=0
    while i<len(L):
        if L[i]==x: del(L[i])
        else: i=i+1
    return L                                                 
L=delete(L,x)
print(L)