a=int(input("Tieu thu="))
if a<=100: t=a*550
elif a<=150: t=100*550 + (a-100)*750
elif a<=200: t=100*550 + 50*750 + (a-150)*950
else: t=100*550 + 50*750 + 50*950 + (a-200)*1350
print("Phai tra=",t+(t*0.1),sep="")