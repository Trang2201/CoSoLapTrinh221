def Nhap():
    a=float(input("a="))
    b=float(input("b="))
    Toantu=input("Toan tu: ")
    return a,b,Toantu
def Ketqua(a,b,Toantu):
    if Toantu=='+': print(a,"+",b,"=",(a+b),sep="")
    elif Toantu=='-': print(a,"-",b,"=",(a-b),sep="")
    elif Toantu=='*': print(a,"*",b,"=",(a*b),sep="")
    elif Toantu=='/': 
        if b==0: print('Khong hop le')
        else: print(a,"/",b,"=",(a/b),sep="")
def Continue():
    Tieptuc=input("Tiep tuc: ")
    return Tieptuc
while True:
    a,b,Toantu=Nhap()
    Ketqua(a,b,Toantu)
    Tieptuc=Continue()
    if Tieptuc=='t' or Tieptuc=='T': break

    