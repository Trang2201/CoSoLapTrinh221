#cách 1:
i=9
while i>=1:
    print('$'*i)
    i=i-1
#cách 2: 
i=1
while i<=9:
    j=1
    while j<=(10-i):
        print('$',end="")
        j=j+1
    print()
    i=i+1
        