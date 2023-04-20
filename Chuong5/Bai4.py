n=int(input("n="))
L=[]
for i in range(1,n+1):
    a=int(input())
    L.append(a)
def count(L):
    dem=0
    for i in L:
        dem+=1
    return dem
dem=count(L)
print(dem)