year_tax = int(input())
shoes_price = year_tax - year_tax * 0.40
clothes_price = shoes_price - shoes_price * 0.20
price_ball = clothes_price / 4

price_outfit = price_ball / 5
total_price = year_tax + shoes_price + clothes_price + price_ball + price_outfit
print(f"{total_price:.2f}")
