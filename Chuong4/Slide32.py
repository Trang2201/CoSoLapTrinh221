def Ketqua(n,r):
    if n==r: return 'Draw!'
    elif n==1:
        if r==2: return 'Human Win!'
        if r==3: return 'Computer Win!'                          
    elif n==2: 
        if r==1: return 'Computer Win!'
        if r==3: return 'Human Win!'
    else:
        if r==1: return 'Human Win!'
        if r==2: return 'Computer Win!'

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



        
    
    