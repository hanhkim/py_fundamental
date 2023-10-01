#Viết chương trình nhập vào số tiền muốn đổi, đổi ra các số tờ mệnh giá: 500.000, 200.000, 100.000, 50.000 và số tiền còn thừa;

cash_number = [500000, 200000, 100000, 50000]

def covertMoney(cash):
    index=0
    count_cash={
        cash_number[0]: 0,
        cash_number[1]: 0,
        cash_number[2]: 0,
        cash_number[3]: 0,
    }
    
    while(index < len(cash_number)):
        count_cash[cash_number[index]]=cash//cash_number[index]    
        cash=cash-cash_number[index]*count_cash[cash_number[index]]
        print(cash, cash//cash_number[index])
        index+=1
    
    result=dict({
        "change": cash,
        cash_number[0]: count_cash[cash_number[0]],
        cash_number[1]: count_cash[cash_number[1]],
        cash_number[2]: count_cash[cash_number[2]],
        cash_number[3]: count_cash[cash_number[3]]
    })
    print(result)
    return result

cash=int(input("Nhập số tiền muốn chuyển đổi: "))

result=covertMoney(cash)

        
        
    