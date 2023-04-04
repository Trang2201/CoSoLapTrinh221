Songaynghi=int(input())
if Songaynghi==0: print("Xep loai A")
elif Songaynghi<2: print("Xep loai B")
elif Songaynghi<4:  print("Xep loai C")
else: print("Xep loai D")
# cách hai:
a=int(input())  # a là số ngày nghỉ
if a==0: s='A'
elif a<2: s='B'
elif a<4: s='C'
else: s='D'
print("Xep loai",s)
