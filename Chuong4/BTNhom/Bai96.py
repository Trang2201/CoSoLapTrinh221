def Nhap():
    s=input()
    return s
def Kiemtra(s):
    a=0
    b=0
    c=0
    for i in range(len(s)):
        if len(s)<8: break
        for j in range(65,91):
            if s[i] in (chr(j)): a+=1
        for j in range(97,123):
            if s[i] in (chr(j)): b+=1
        for j in range(48,58):
            if s[i] in (chr(j)): c+=1
    return a,b,c
def Inkq(a,b,c):
    if a!=0 and b!=0 and c!=0:
        print("True")
    else: print("False")
s=Nhap()
a,b,c=Kiemtra(s)
Inkq(a,b,c)