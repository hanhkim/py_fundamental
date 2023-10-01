name=input("Tên hàng: ")
quantity=int(input("Số lượng: "))
price=float(input("Đơn giá: "))
print("Thành tiền: {0:,.0f} ({1} cái {2})".format(quantity*price, quantity, name))