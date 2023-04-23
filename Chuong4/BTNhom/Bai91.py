def Nhap():
    s=input()
    return s
def precedence(s):
    if s in ('+','-'): return 1
    elif s in ('*','/'): return 2
    elif s=='^': return 3
    elif s not in ('+','-','*','/','%','//','^'):
        return 'Khong hop le!'
    else: return -1
s=Nhap()
kq=precedence(s)
print(kq)
