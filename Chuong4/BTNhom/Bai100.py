def Nhap():
    m=int(input("month: "))
    y=int(input("year: "))
    return m,y
def dom(m,y):
    if m in [1,3,5,7,8,10,12]: d=31
    elif m in [4,6,9,11]: d=30
    elif m==2:
        mod=y%100
        if mod%4==0: d=29
        elif mod==0:
            if y%4==0: d=29
        else: d=28
    return d
m,y=Nhap()
d=dom(m,y)
print("So ngay=",d)