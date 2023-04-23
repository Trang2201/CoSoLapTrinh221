from Bai94 import password
from Bai96_2 import Kiemtra
def main():
    dem=0
    while True:
        L=password()
        s="".join(L)
        dem+=1
        a,b,c=Kiemtra(s)
        if a and b and c: break
    return dem,s
def Inkq(dem,s):
    print(s)
    print(dem)
dem,s=main()
Inkq(dem,s)

    