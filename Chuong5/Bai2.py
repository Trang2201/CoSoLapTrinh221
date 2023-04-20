x=int(input("x="))
n=int(input("n="))
L=[]
for i in range(1,n+1):
    a=int(input())
    L.append(a)
def search(L,x):                        
    for i in range(len(L)):
        if L[i]==x: return i
    return None
kq=search(L,x)
print("Ket qua tim kiem:",kq)


        