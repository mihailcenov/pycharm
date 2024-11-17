type_price = input()
rows = int(input())
columns = int(input())

income = 0
capacity = rows * columns
if type_price == "Premiere":
    income = capacity * 12
elif type_price == "Normal":
    income = capacity * 7.50
elif type_price == "Discount":
    income = capacity * 5.00


print(f"{income:.2f}")