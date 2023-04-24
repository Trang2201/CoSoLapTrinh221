def Nhap():
    a=int(input("Luong:"))
    b=input("Don vi:")
    return a,b
def quydoi(a,b):
    if b=='teaspoon': 
        cup=a//48
        table=(a%48)//3
        tea=(a%48)%3
    elif b=='tablespoon':
        cup=a//16
        table=a%16
        tea=0
    else: 
        cup=a
        table=0
        tea=0
    return cup,table,tea
a,b=Nhap()
cup,table,tea=quydoi(a,b)
print(cup,"cup,",table,"tablespoon,",tea,"teaspoon")
        