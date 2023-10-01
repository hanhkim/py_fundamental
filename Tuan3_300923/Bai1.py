# Viet chuong trinh countdown tu n ve 1 (n>0) theo 2 cach

while True:
    n=int(input("Nhập vào số nguyên n > 0: "))
    if n > 0:
        break
    else: 
        print("Vui long nhap so nguyen n > 0")

for i in range(n, -1, -1):
    print("Count down: ", i)
