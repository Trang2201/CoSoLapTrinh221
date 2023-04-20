def Input():
    L=[]
    n=int(input("n="))
    for i in range(n):
        a=int(input())
        L.append(a)
    x=int(input("x="))
    return L,x
def FirstAndLast(L):
    M=[]
    M = M + [L[0]] + [L[-1]]
    # M = L[:1] + L[-1:]
    print(M)
def Search(L,x):
    if x in L: return True
    else: return False
    
L,x=Input()
FirstAndLast(L)
kq=Search(L,x)
print(kq)
    
        