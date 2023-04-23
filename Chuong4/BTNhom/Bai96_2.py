def Nhap():
    s=input()
    return s
def Kiemtra(s):
    a=False
    b=False
    c=False
    if len(s)<8: return a,b,c
    for i in range(len(s)):
        for j in range(65,91):
            if s[i] in (chr(j)): a=True
        for j in range(97,123):
            if s[i] in (chr(j)): b=True
        for j in range(48,58):
            if s[i] in (chr(j)): c=True
    return a,b,c
def Inkq(a,b,c):
    if a==True and b==True and c==True: print("True")
    else: print("False")
s=Nhap()
a,b,c=Kiemtra(s)
Inkq(a,b,c)