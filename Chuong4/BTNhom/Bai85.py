def Nhap():
    a=int(input("a="))
    if a==1: num='1st'
    elif a==2: num='2nd'
    elif a==3: num='3rd'
    else: num=''
    for i in range(4,13):
        if i==a: num=str(i) + 'th'
    print(a,num) 
      
def STT():
    for num in range(1,13):
        if num==1: i='1st'
        elif num==2: i='2nd'
        elif num==3: i='3rd'
        else: i=str(num) + 'th'
        print(num,i)
        
# def STT(i):
#     if i==1: num='1st'
#     elif i==2: num='2nd'
#     elif i==3: num='3rd'
#     else: num=str(i) + 'th'
#     return num    
# for i in range(1,13):
#     num=STT(i)
#     print(i,num)
    
#Nhap()
#STT()
