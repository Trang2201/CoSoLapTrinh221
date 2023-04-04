#in ra kim tự tháp với while.
n=int(input("n="))
i=1
while i<=n:
    j=1
    while j<=(n-i):
        print(" ",end="")
        j=j+1
    print("*"*(2*i-1))
    i=i+1

        