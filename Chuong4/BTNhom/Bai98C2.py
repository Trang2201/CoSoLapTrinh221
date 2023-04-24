def Nhap():
    s=input()
    return s
def hex2int(a):
    L=['A','B','C','D','E','F']
    n=['a','b','c','d','e','f']
    M=[i for i in range(10,16)]
    if a in L:
        for i in range(len(L)):
            if L[i]==a: a=M[i]
    else: 
        for i in range(len(n)):
            if n[i]==a: a=M[i]    
    return a
def int2hex(a):
    L=[str(i) for i in range(10,16)]
    M=['A','B','C','D','E','F']
    for i in range(len(L)):
        if L[i]==a: a=M[i]
    return a
    
a=Nhap()
L=[str(i) for i in range(0,16)]
M=[i for i in range(0,10)]
N=['A','B','C','D','E','F']
n=['a','b','c','d','e','f']
if a not in L and a not in N and a not in n:
        print("Khong hop le!")
else:
    if a in N or a in n:
        b=hex2int(a)
        print("Chuyen sang he thap phan:",b)
    elif a in L:
        s=int2hex(a)
        print("Chuyen sang he thap luc:",s)