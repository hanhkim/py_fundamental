while True:
    x,y=eval(input("Nhap pham vi tu x den y de tinh tong binh phuong: "))
    if x >= y:
        print("Vui long nhap x < y")
    s = 0
    for i in range(x, y+1):
        print(i)
        s+=i**2
    break
print("Tong binh phuong tu {} -> {} = {}".format(x, y, s))

