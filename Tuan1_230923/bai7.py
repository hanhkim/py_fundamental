Alice_candies_count=int(input("Nhập số kẹo của Alice: "))
Bob_candies_count=int(input("Nhập số kẹo của Bob: "))
Carol_candies_count=int(input("Nhập số kẹo của Carl: "))

candy_total=Alice_candies_count + Bob_candies_count + Carol_candies_count
print("Tổng số kẹo là: ", candy_total)
print("Số kẹo dư và cần huỷ bỏ là: {} ,mỗi người sẽ có {:.0f} kẹo".format(candy_total%3, (candy_total - candy_total%3)/3))