#in ra màn hình tổng các số nguyên tố từ 2 đến n.
n=int(input("n="))
is_prime=0
a=0
for num in range(2,n+1):
    s=0
    for i in range(2,num):
        if num%i==0: s=s+1
    if s==0: 
        is_prime=num
        a=a+is_prime
print("Tong cac so nguyen to tu 2 den",n,"=",a)