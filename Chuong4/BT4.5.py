def SoHopLe(x):
    return x<=1
def LaSoNguyenTo(x):
    for i in range(2,x):
        if x%i==0: return False
    return True
def NhapVaDem():
    print("Nhap day so:")
    count=0
    while True:
        x=int(input())
        if SoHopLe(x): break
        if LaSoNguyenTo(x): count=count+1
    return count
def InKQ(kq): print("Co",kq,"so nguyen to")
kq=NhapVaDem()
InKQ(kq)
