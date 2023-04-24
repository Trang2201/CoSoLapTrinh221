#Viết một hàm có chức năng tối giản phân số với hai tham số duy nhất là một tử số và một mẫu số 
#được nhập vào từ bàn phím 
#và cho ra kết quả là phân số được tạo thành từ tử và mẫu số trên sau khi tối giản.
def Nhap():
    t=int(input("Tu so:"))
    m=int(input("Mau so:"))
    return t,m
def toigian(t,m):
    i=2
    j=2
    while i<=t and j<=m:
        if t%i==0 and m%j==0:
            if i==j: 
                t=int(t/i)
                m=int(m/j)
        else: 
            i+=1
            j+=1
    return t,m
t,m=Nhap()
a,b=toigian(t,m)
print("Phan so toi gian=",a,"/",b,sep="")