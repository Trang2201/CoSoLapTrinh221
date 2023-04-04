for i in range(1,10):  #in theo thứ tự từ 1 đến 9
    print('$'*(10-i))
# cách hai:
for i in range(9,0,-1): #in ngược lại
    print('$'*i)
#bài toán nhập số nguyên n để in ra n dòng ký tự:
n=int(input("n="))
for i in range(1,n+1):
    for j in range(1,n+2-i): 
        print('*',end="")
    print()