def Nhap():
    s=input()
    return s
def isInteger(s):
    s=s.strip()
    if s[0]=='+' or s[0]=='-':
        s=s.replace(s[0],"")
        n=s.isdigit()
        return n
    else:
        n=s.isdigit()
        return n
def Inkq(kq):
    print(kq)
s=Nhap()
kq=isInteger(s)
Inkq(kq)