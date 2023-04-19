def Nhap():
    s=input()
    return s
def Inhoa(s):
    s=s.capitalize()
    for i in range(len(s)):
        if s[i] in ('.', '!', '?'):
            j=i+1
            while j < len(s) and s[j].isspace():
                j=j+1
            if j < len(s):
                s = s[:j] + s[j:].capitalize()          #xuất tập con bằng cú pháp kiểu list
    s=s.replace(' i ',' I ')
    return s
def Inkq(kq):
    print(kq)
s=Nhap()
kq=Inhoa(s)
Inkq(kq)