# Viết chương trình in bảng cửu chương từ 2 đến n (Xuất ra theo cột)
while True:
    n=int(input("Nhập số nguyên n: "))
    if n <= 2:
        print("Nhập số nguyên n > 2 nha, please")
        continue
    break

for i in range(1,10):
    for j in range(2, n+1):
        print("{}x{}={}".format(i, j, i *j), end='\t')
    print("\n")