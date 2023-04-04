#in ra màn hình số nguyên tố lớn nhất trong dãy từ 2 đến n
n=int(input("Nhập n: "))
max=2
for num in range(2,n+1):
    s=0
    for i in range(2,num):
        if num%i==0:
            s=s+1
            break
    if s==0:
        max=num
print("Số nguyên tố lớn nhất từ 2 đến",n,"là:",max)
