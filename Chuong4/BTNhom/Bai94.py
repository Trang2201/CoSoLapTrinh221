def password():
    import random
    s=str(random.randint(1000000,9999999999))
    L=[]
    for i in range(len(s)):
        L.append(chr(random.randint(33,126)))
    return L
def Inkq(L):
    for i in L: print(i,end="")   
L=password()
Inkq(L)

        
                