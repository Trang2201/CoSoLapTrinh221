Tieptuc=""
while Tieptuc!='t' and Tieptuc!='T':
    a=float(input("a="))
    b=float(input("b="))
    Toantu=input("Toan tu: ")
    if Toantu=='+': print(a,Toantu,b,"=",(a+b),sep="")
    elif Toantu=='-': print(a,Toantu,b,"=",(a-b),sep="")
    elif Toantu=='*': print(a,Toantu,b,"=",(a*b),sep="")
    elif Toantu=='/': 
        if b==0: print('Khong hop le')
        else: print(a,Toantu,b,"=",(a/b),sep="")
    Tieptuc=input("Tiep tuc: ")