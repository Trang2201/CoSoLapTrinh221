def Ketqua(n,r):
    if n==r: 
        return 'Draw!'
    elif (n==1 and r==2) or (n==2 and r==3) or (n==3 and r==1):           
        return 'Human Win!'
    else: 
        return 'Computer Win!'

def Inkq(kq):
    print("Result:",kq)

import random
while True:
    n=int(input("Human: "))
    if n==0: break
    else: 
        r=random.randint(1,3)
        print("Computer:",r)
    kq=Ketqua(n,r)
    Inkq(kq)