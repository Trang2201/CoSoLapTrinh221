#a:
n=int(input("n="))
for i in range(1,n+1):
    print(i)
#b:
n=int(input("n="))
for i in range(1,n+1):
    if i%5==0:
        print(i)
    else: print(i,end=" ")
#c:
n=int(input("n="))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()