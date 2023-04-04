n=int(input("n="))
max=1
for num in range(2,n+1):
    s=0
    for i in range(2,num):
        if i*i==num:
            s=s+1
    if s!=0: max=num
print("So chinh phuong lon nhat tu 1 den",n,"la:",max)
         