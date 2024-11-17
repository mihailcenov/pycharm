area = float(input())

price_per_meter = area * 7.61
discount = price_per_meter * 0.18
total_price = price_per_meter - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")