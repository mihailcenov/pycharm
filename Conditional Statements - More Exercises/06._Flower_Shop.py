import math

number_magnolias = int(input())
number_hyacinth = int(input())
number_roses = int(input())
number_cactus = int(input())
price_present = float(input())

price_magnolias = number_magnolias * 3.25
price_hyacinth = number_hyacinth * 4.0
price_roses = number_roses * 3.50
price_cactus = number_cactus * 8.0


total_price = price_magnolias + price_hyacinth + price_roses + price_cactus
profit_after_tax = total_price * 0.95

if price_present > profit_after_tax:
        not_enough_money = price_present - profit_after_tax
        print(f"She will have to borrow {math.ceil(not_enough_money)} leva.")
else:
    left_money = profit_after_tax - price_present
    print(f"She is left with {math.floor(left_money)} leva.")