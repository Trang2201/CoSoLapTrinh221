def Nhap():
    s=input()
    n=int(input())
    return s,n
def hex2int(s):
    if s=='A' or s=='a': s=10
    elif s=='B' or s=='b': s=11
    elif s=='C' or s=='c': s=12
    elif s=='D' or s=='d': s=13
    elif s=='E' or s=='e': s=14
    elif s=='F' or s=='f': s=15
    return s
def int2hex(n):
    if n==10: n='A'
    elif n==11: n='B'
    elif n==12: n='C'
    elif n==13: n='D'
    elif n==14: n='E'
    elif n==15: n='F'
    return n
s,n=Nhap()
L=[i for i in range(0,16)]
M=[i for i in range(0,10)]
N=['A','B','C','D','E','F']
P=['a','b','c','d','e','f']
if s not in str(L) and s not in N and s not in P and n not in L:
        print("Khong hop le!")
if s not in str(M) and s not in N and s not in P:
    print("Khong the chuyen sang he thap phan")
else:
    b=hex2int(s)
    print("Chuyen sang he thap phan:",b)
if n not in L:
    print("Khong the chuyen sang he thap luc")
else:
    c=int2hex(n)
    print("Chuyen sang he thap luc:",c)

    
    