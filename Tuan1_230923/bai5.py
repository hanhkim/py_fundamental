# Viết chương trình tính lãi suất ngân hàng
# Lãi suất một năm, số tiền gửi và số tháng gửi được nhập vào từ bàn phím. Viết chương trình tính tiền lãi và tính tổng sô tiền nhận được sau khi hết thời hạn gửi tiền.
# Tiền lãi = (Số tiền gửi * Số tháng) * (Lãi suất năm / 12)
# Tổng số tiền  = số tiền gửi + tiền lãi

lai_suat_ngan_hang=float(input("Nhập lãi suất ngân hàng VCB (theo năm): "))
so_tien_gui=int(input("Số tiền bạn gửi là: "))
so_thang_gui=int(input("Só tháng bạn gửi là: "))

tien_lai=(so_tien_gui*so_thang_gui*(lai_suat_ngan_hang/100)/12)
print("Tiền lãi sau {} tháng là: {:,.0f} VND".format(so_thang_gui, tien_lai))
print("Tổng số tiền: {:,.0f} VND".format(so_tien_gui + tien_lai))