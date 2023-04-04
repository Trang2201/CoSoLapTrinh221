def nhap():
    n=int(input("n="))
    return n
def inkq(n):
    while True:
        for i in range(1,n+1):
            if i%2==0:
                print(i,end=" ")
        print()
        print("Tiep tuc khong?",end="")
        a=input()
        if a=='k' or a=='K':
            break
        else: n=int(input("n="))
n=nhap()
inkq(n)

        
