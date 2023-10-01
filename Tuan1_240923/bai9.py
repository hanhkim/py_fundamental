#Nhập vào một số nguyên x. Tính và in ra S = 1 + x + x^3/3 + x^5/5

def calFun(x):
    return 1 + x + pow(x,3)/3 + pow(x,5)/5

x=int(input("Nhập số nguyên x: "))
print("Kết quả công thức là: S = 1 + x + x^3/3 + x^5/5 với x={} là {:.2f}".format(x,  calFun(x)))