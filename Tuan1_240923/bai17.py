import math

def giaiPhuongTrinhBac1(a, b):
    if a == 0 and b == 0:
        print("Phương trình vô số nghiệm")
        return
    elif a == 0 and b!= 0:
        print("Phương trình vô nghiệm")
        return
    else:
        print("Phương trình có nghiệm là: {}".format(-b/a))

# print("Phương trình bậc 1 có dạng là: ax + b = 0")
# a=float(input("Nhập a: "))
# b=float(input("Nhập b: "))
# giaiPhuongTrinhBac1(a, b)


def giaiPhuongTrinhBac2(a,b,c):
    if a == 0 and b == 0 and c==0:
        print("Phương trình có vô số nghiệm")
    elif a == 0: 
        giaiPhuongTrinhBac1(b,c)
    else:
        delta= b**2 - 4 * a * c
        print("deleta ", delta)
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0: x
            print("Phương trình có nghiệm kép là {}".format(-b/(2*a)))
        else:
            print("Phương trình có nghiệm là:")
            print("x1 = {}".format((-b + math.sqrt(delta))/(2*a)))
            print("x2 = {}".format((-b - math.sqrt(delta))/(2*a)))


print("Phương trình bậc 2 có dạng là: ax^2 + bx + c = 0")
a=float(input("Nhập a: "))
b=float(input("Nhập b: "))
c=float(input("Nhập c: "))
print("Đant tính toán phương trình ..... ")
giaiPhuongTrinhBac2(a,b,c)

