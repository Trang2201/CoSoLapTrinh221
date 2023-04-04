i='*'
while i!='*'*7:
    print(i)
    i=i+'*'
# cách hai:
i=1
while i<=6:
    j=1
    while j<=i:
        print('*',end="")
        j=j+1
    print("")
    i=i+1
