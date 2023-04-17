n=int(input("n="))
s=0  
if (n<2): s=1 
for i in range(2,n):
    if (n%i==0): 
        s=1
        break
if s==0: print(n,"la SNT")
else: print(n,"khong la SNT")


