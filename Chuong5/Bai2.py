x=int(input())
n=int(input())
L=[]
for i in range(1,n+1):
    a=int(input())
    L=L+[a]
# def search(L,x):                       #trả về index đầu tiên khi tìm thấy x trong list L
#     s=L.index(x)
#     return s
# def Inkq(s):
#     print(s)
# s=search(L,x)
# Inkq(s)

def search(L,x):                         #trả về từng index của x trong list L
    s=0
    for i in range(len(L)):
        if L[i]==x: 
            s=s+1
            print(i,end=" ")
    if s==0: print("None")
search(L,x)
        