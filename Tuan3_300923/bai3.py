def tongSoLe(n):    
    tong_so_le_nho_hon_n = 0
    kq_str="A = "

    for i in range(1, n+1):
        if i % 2 == 1:
            tong_so_le_nho_hon_n+=i
            kq_str += str(i) + " + "

    kq_str = kq_str[:-2] + "="
    print("******************************")
    print(kq_str,tong_so_le_nho_hon_n)
    print("******************************")

def tongSoChan(n):
    tong_so_chan_nho_hon_n = 0
    kq_str="B = "

    for i in range(1, n+1):
        if i % 2 == 0:
            tong_so_chan_nho_hon_n+=i
            kq_str += str(i) + " + "

    kq_str = kq_str[:-2] + "="

    print("******************************")
    print(kq_str,tong_so_chan_nho_hon_n)
    print("******************************")


def tichSoTu1DenN(n):
    tich_tu_1_den_n = 1
    kq_str= "C = "

    for i in range(1, n+1):
        tich_tu_1_den_n*=i
        kq_str += str(i) + " * "

    kq_str = kq_str[:-2] + "="

    print("******************************")
    print(kq_str,tich_tu_1_den_n)
    print("******************************")
    
def tichSoChiaHet3VaNhoHoacBangN(n):
    tich = 1
    kq_str= "D = "

    for i in range(1, n+1):
        if i % 3 == 0:
            tich *= i
            kq_str += str(i) + " * "
        

    kq_str = kq_str[:-2] + "="

    print("******************************")
    print(kq_str,tich)
    print("******************************")

def runMain():
    while True:
        print("***************** HELLO BAITAP 3 ******************")
        print("** Tổng các số lẻ nhỏ hơn hay bằng n, ************** nhấn 1")
        print("** Tổng các số chẵn nhỏ hơn hay bằng n, ************ nhấn 2")
        print("** Tích các số từ 1 đến n, ************************* nhấn 3")
        print("** Tích các số chia hết cho 3 nhỏ hơn hay bằng n, ** nhấn 4")
        print("** Tiếp tục chương trình, ************************** nhấn Y")
        print("** Thoát chương trình, ***************************** nhấn N")

        _shouldContinue=input("Vui lòng nhập chương trình: ")
        
        if _shouldContinue == "N" or _shouldContinue == "n":
            break
        elif _shouldContinue == "Y" or _shouldContinue == "y":
            continue    

        while True:
            n=int(input("Nhập số nguyên n: "))
            if n <= 0:
                print("Nhập số nguyên n > 0 nha, please")
                continue
            break

        if _shouldContinue == "1":
            tongSoLe(n)
        if _shouldContinue == "2":
            tongSoChan(n)
        elif _shouldContinue == "3":
            tichSoTu1DenN(n)
        elif _shouldContinue == "4":
            tichSoChiaHet3VaNhoHoacBangN(n)
       
runMain()
