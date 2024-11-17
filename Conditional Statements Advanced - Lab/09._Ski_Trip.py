# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка

stayed_days = int(input())
type_residence = input()
evaluation = input()
price = 0.0
night = stayed_days - 1
discount = 0.0
if type_residence == "room for one person":
    price = 18.00
    if stayed_days < 10:
        discount = 0.0
    elif stayed_days < 15:
        discount = 0.0
    else:
        discount = 0.0
elif type_residence == "apartment":
    price = 25.00
    if stayed_days < 10:
        discount = 0.30
    elif stayed_days < 15:
        discount = 0.35
    else:
        discount = 0.50
elif type_residence == "president apartment":
    price = 35.00
    if stayed_days < 10:
        discount = 0.10
    elif stayed_days < 15:
        discount = 0.15
    else:
        discount = 0.20

total_price = price * night * (1 - discount)

if evaluation == "positive":
    total_price = total_price * 1.25
elif evaluation == "negative":
    total_price = total_price * 0.90

print(f"{total_price :.2f}")









