def STT(i):
    if i==1: num='1st'
    elif i==2: num='2nd'
    elif i==3: num='3rd'
    else: num=str(i) + 'th'
    return num    
for i in range(1,13):
    num=STT(i)
    print(i,num)
    