
group_budget = int(input())
season = input()
number_fisherman = int(input())

ship_price = 0.0
discount = 0.0
extra_discount = 0.0
if season == "Spring":
    ship_price = 3000
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
elif season == "Winter":
    ship_price = 2600

if number_fisherman <= 6:
    discount = 0.10
elif 7 <= number_fisherman <= 11:
    discount = 0.15
else:
    discount = 0.25

if number_fisherman % 2 == 0 and season != "Autumn":
    extra_discount = 0.05

total_price = ship_price * (1 - discount) * (1 - extra_discount)

if group_budget >= total_price:
    money_left = group_budget - total_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    needed_money = total_price - group_budget
    print(f"Not enough money! You need {needed_money:.2f} leva.")