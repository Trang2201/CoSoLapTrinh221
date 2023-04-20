def Input():
    L=[]
    n=int(input("n="))
    for i in range(n):
        a=int(input())
        L.append(a)
    return L
def Search(L):
    L.sort()
    min=L[0]
    max=L[-1]
    return max, min
def Output(max, min):
    print(max,min)
L=Input()
max,min=Search(L)
Output(max,min)
    