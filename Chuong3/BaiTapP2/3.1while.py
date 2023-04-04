n=int(input("n="))
while True:
    if (n>=1) and (n<=50):
        break
    else:
        print("Khong hop le\nMoi nhap lai")
        n=int(input("n="))
# cách hai:
n=int(input("n="))
while (n<1) or (n>50):
    print("Khong hop le!\nMoi nhap lai")
    n=int(input("n="))