def Nhap():
    num=int(input("Nhap so luong san pham: "))
    return num
def PhiShip(num):
    base=10.95
    TC=base + (num-1)*2.95
    return TC
def Inkq(TC):
    print("Phi ship phai tra= $",TC,sep="")
num=Nhap()
TC=PhiShip(num)
Inkq(TC)
    