x=int(input("x="))
n=int(input("n="))
L=[]
y=int(input("y="))                   #đề không yêu cầu x,y là số nguyên hay chuỗi.
for i in range(n):
    a=int(input())
    L=L+[a]
def replace(L,x,y):
    for i in range(len(L)):
        if L[i]==x: L[i]=y
    return L
L=replace(L,x,y)
print(L)