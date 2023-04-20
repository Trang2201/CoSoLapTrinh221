x=int(input("x="))
n=int(input("n="))
L=[]
for i in range(1,n+1):
    a=int(input())
    L.append(a)
def delete(L,x):                    #cộng những phần tử khác x vào một list mới.
    M=[]
    for i in L:
        if i!=x: M.append(i)
    return M
M=delete(L,x)
print(M)
        