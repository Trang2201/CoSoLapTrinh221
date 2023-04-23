def Nhap():
    s=input()
    return s
def Kiemtra(s):
    for i in range(len(s)):
        if s[i] not in ('1','2','3','4','5','6','7','8','9','0'):
            return False
    return True
def isInteger(s):
    s=s.strip()
    if len(s)==0: return False
    if s[0] in ('+','-'):
        if len(s)==1: return False
        else: 
            s=s.replace(s[0],"")
    kq=Kiemtra(s)
    return kq

s=Nhap()
kq=isInteger(s)
print(kq)