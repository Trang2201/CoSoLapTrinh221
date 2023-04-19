x=int(input())
n=int(input())
L=[]
y=int(input())                   #đề không yêu cầu x,y là số nguyên hay chuỗi.
for i in range(n):
    a=int(input())
    L=L+[a]
def replace(L,x,y):
    for i in range(len(L)):
        if L[i]==x: L[i]=y
    return L
def Inkq(L):
    print(L)
L=replace(L,x,y)
Inkq(L)