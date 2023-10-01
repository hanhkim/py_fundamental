# Viết chương trình tính chu vi và diện tích của hình chữ nhật

# eval: nhập đồng thời cùng nhiều biến
#chieu_dai,chieu_rong=eval(input('Nhap chieu dai, chieu rong: ))

chieu_dai=float(input("Nhập chiều dài: "))
chieu_rong=float(input("Nhập chiều rộng: "))

print("Chu vi hcn = ", (chieu_dai+chieu_rong)*2)
print("Diện tích hcn = ", chieu_dai*chieu_rong)