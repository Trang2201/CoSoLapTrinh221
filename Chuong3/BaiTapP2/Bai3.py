n=int(input("Nhap n (0<=n<=9999): "))
m=n
s=0
if n==0: s=1
while n>0:
    n=n//10
    s=s+1
print(m,"co",s,"chu so")
        
        