def lyrics():
    gifts=[ "And a partridge in a pear tree",
            "Two turtledoves",
            "Three French hens",
            "Four calling birds",
            "Five golden rings",
            "Six geese a-laying",
            "Seven swans a-swimming",
            "Eight maids a-milking",
            "Nine ladies dancing",
            "Ten lords a-leaping",
            "Eleven pipers piping",
            "Twelve drummers drumming" ]
    return gifts
# def doansau(gifts):        #In ra màn hình full lyrics của bài hát
#     print("On the first day of Christmas, my true love sent to me\nA partridge in a pear tree")
#     for i in range(2,13):
#         if i==2: num='2nd'
#         elif i==3: num='3rd'
#         else: num=str(i) + 'th'
#         print("On the",num,"day of Christmas, my true love sent to me")
#         for j in range(i-1,-1,-1):
#             print(gifts[j])
# gifts=lyrics()
# doansau(gifts)

def Nhap(gifts):        #Nhập một số nguyên n và in ra màn hình đoạn nhạc tương ứng với n
    n=int(input("n="))
    if n==1: print("On the first day of Christmas, my true love sent to me\nA partridge in a pear tree")
    else: 
        for i in range(n,n+1,1):
            if i==2: num='2nd'
            elif i==3: num='3rd'
            else: num=str(i) + 'th'
            print("On the",num,"day of Christmas, my true love sent to me")
            for j in range(i-1,-1,-1):
                print(gifts[j])
gifts=lyrics()
Nhap(gifts)
        
