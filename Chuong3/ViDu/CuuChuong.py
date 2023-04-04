#nhập vào số n và in ra màn hình bảng cửu chương n.
n=int(input())
for i in range(1,n+1):
    for j in range(1,10):
        print(i*j,end=" ")
    print()
    