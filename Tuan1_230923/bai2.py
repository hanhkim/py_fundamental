so_1=float(input("Nhap so thu nhat: "))
so_2=float(input("Nhap so thu hai: "))

#using normal
print('Tong: ', so_1+so_2)
print('Hiệu: ', so_1-so_2)
print('Tich: ', so_1*so_2)
print('Thương: ', so_1/so_2)

#using  %
print('Thương: %.2f'%(so_1/so_2))

#using .format
print('{:.1f}*{:.1f}={:.1f}'.format(so_1,so_2,so_1*so_2))

print('Thương: {:.2f}'.format(so_1/so_2))