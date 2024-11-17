voucher_value = int(input())
tickets_count = 0
purchases_count = 0
price = 0
while True:
    purchase_name = input()
    if purchase_name == "End":
        break
    if len(purchase_name) > 8:
        price = ord(purchase_name[0]) + ord(purchase_name[1])
    else:
        price = ord(purchase_name[0])
    if voucher_value < price:
        break
    voucher_value -= price

    if len(purchase_name) > 8:
        tickets_count += 1
    else:
        purchases_count += 1

print(tickets_count)
print(purchases_count)