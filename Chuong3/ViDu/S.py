#in ra màn hình dãy các số nguyên tố từ 2 tới n
n=int(input("n="))
a=0
for num in range(2,n+1):
    s=0
    for i in range(2,num):
        if num%i==0: 
            s=s+1
    if s==0: 
        a=num
        print(a)
        
        
        
    