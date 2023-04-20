def Nhap():
    L=[]
    n=int(input("n="))
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def SND(L):
    dem=0
    for i in L:
        if i>0: dem+=1
    print("SND=" + str(dem))
def TBC(L):
    s=0
    dem=0
    for i in range(len(L)):
        if L[i]%2==0: 
            s=s+L[i]
            dem=dem+1
    if dem==0: print("TBC=0")
    else: 
        tbc=s/dem
        print("TBC=" + str(tbc))
L=Nhap()
SND(L)
TBC(L)


        