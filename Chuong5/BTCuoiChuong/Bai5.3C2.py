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
    return dem
def TBC(L):
    s=0
    dem=0
    for i in range(len(L)):
        if L[i]%2==0: 
            s=s+L[i]
            dem=dem+1
    if dem==0: return 0
    tbc=s/dem
    return tbc
L=Nhap()
dem=SND(L)
print("SND=" + str(dem))
tbc=TBC(L)
print("TBC=" + str(tbc))