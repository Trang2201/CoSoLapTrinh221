def Nhap():
    a=float(input("Nhap do dai quang duong theo don vi km: "))
    return a
def Giatien(a):
    base=4
    p_m=0.25/140
    s=a*1000
    TC=base + p_m*s
    return TC
def Inkq(TC):
    print("Tong gia cuoc taxi= $",TC,sep="")
a=Nhap()
TC=Giatien(a)
Inkq(TC)
    
    
