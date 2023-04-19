def Nhap():                    #không dùng hàm center
    s=input()
    a=int(input())
    return s,a
def center(s,a):
    n=len(s)
    if (a-n)%2==0: khoangcach=" " * ((a-n)/2)
    else: khoangcach=" " * int(((a-n)/2)+0.5)
    if a<n: print(s)
    else: 
        s= khoangcach + s
        print(s)
s,a=Nhap()
center(s,a)

# def center(s,a):                #dùng hàm center
#     n=len(s)
#     if a<n: print(s)
#     else: 
#         print(s.center(a))
# s,a=Nhap()
# center(s,a)
    