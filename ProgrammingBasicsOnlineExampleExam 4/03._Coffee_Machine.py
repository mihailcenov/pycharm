drink = input() # Espresso, Cappuccino, Tea
sugar = input() # Without, Normal, Extra
number_drinks = int(input())
price = 0

if drink == "Espresso":
    if sugar == "Without":
        price = 0.90
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60
elif drink == "Tea":
    if sugar == "Without":
        price = 0.50
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

total_price = price * number_drinks

if sugar == "Without":
    total_price -= (total_price * 35) / 100

if drink == "Espresso" and number_drinks > 5:
    total_price -= (total_price * 25) / 100

if total_price > 15:
    total_price -= (total_price * 20) / 100

print(f"You bought {number_drinks} cups of {drink} for {total_price:.2f} lv.")
