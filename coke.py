startPrice = 50
currentPrice = 50
paid_amount = 0
coin = [25, 10, 5]

while paid_amount < startPrice:
    print(f"Amount Due: {currentPrice}")
    paid_amount = int(input("Insert Coin: "))
    
    if paid_amount == coin[0] or paid_amount == coin[1] or paid_amount == coin[2]:
        currentPrice -= paid_amount
        if currentPrice == 0:
            print(f"Change Owed: {currentPrice}")
            break

