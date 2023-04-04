#nhập vào màn hình số n và in ra kết quả có phải số chính phương hay không.
n=int(input("n="))
s=0
for i in range (1,n+1):
    if i*i==n: 
        s=s+1
        a=i
if s!=0: print(n,"la so chinh phuong cua",a)
else: print(n,"khong la so chinh phuong")
