import random
def Nhap():
    n=int(input("Human: "))
    return n
def Ketqua(n,m):
    if n==m:
        return "Draw!"
    elif (n==2 and m==3) or (n==1 and m==2) or (n==3 and m==1):
        return "Human Win!"
    else:
        return "Computer Win!"
def InKQ(kq):
    print("Result:",kq)
while True:
    n=Nhap()
    if n==0: break
    else:
        m=random.randint(1,3)
        print("Computer:",m)
    kq=Ketqua(n,m)
    InKQ(kq)
    