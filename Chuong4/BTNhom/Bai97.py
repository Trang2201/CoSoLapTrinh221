def password():
    import random
    s=str(random.randint(1000000,9999999999))
    L=[]
    for i in range(len(s)):
        L.append(chr(random.randint(33,126)))
    return L
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
def main():
    dem=0
    while True:
        L=password()
        s="".join(L)
        dem+=1
        a,b,c=Kiemtra(s)
        if a and b and c: break
    return dem,s
def Inkq(dem,s):
    print(s)
    print(dem)
dem,s=main()
Inkq(dem,s)