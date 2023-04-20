#while:
a=input()
n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(a,end=" ")
        j=j+1
    print()
    i=i+1
#for:
a=input()
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
    print()
        

