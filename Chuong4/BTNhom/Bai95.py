import random
def generate():
    if random.random()<0.5:
        #tạo biển số xe cũ
        a=str(random.randint(100,999))
        for i in range(3):
            a=chr(random.randint(65,90)) + a
        print(a)
    else:
        #tạo biển số xe mới   
        b=str(random.randint(1000,9999))
        for i in range(3):
            b=b+chr(random.randint(65,90))
        print(b)
generate()