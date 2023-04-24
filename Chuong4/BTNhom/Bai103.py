# def Nhap():
#     m=int(input("Month:"))
#     d=int(input("Date:"))
#     y=int(input("Year:"))
#     return m,d,y
def Kiemtra(m,d,y):
    mod=y%100
    if m*d==mod: print("Ngay",d,"Thang",m,"Nam",y)
def In():
    for y in range(1901,2000):
        for m in range(1,13):
            if m in [1,3,5,7,8,10,12]: 
                for d in range(1,32):
                    Kiemtra(m,d,y)
            elif m in [4,6,9,11]:
                for d in range(1,31):
                    Kiemtra(m,d,y)
            elif m==2:
                mod=y%100
                if mod%4==0: 
                    for d in range(1,30):
                        Kiemtra(m,d,y)
                elif mod==0:
                    if y%4==0: 
                        for d in range(1,30):
                            Kiemtra(m,d,y)
                else: 
                    for d in range(1,29):
                        Kiemtra(m,d,y)
In()
    
    