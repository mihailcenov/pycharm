family_budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percent_extra_costs = int(input())

if number_nights > 7:
    price_per_night -= (price_per_night * 5.0) / 100.0


price_extra_costs = (family_budget * percent_extra_costs) / 100
total_money = (price_per_night * number_nights) + price_extra_costs
# print(total_money)

if family_budget >= total_money:
    money_left = family_budget - total_money
    # print(money_left)
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    needed_money = total_money - family_budget
    print(f"{needed_money:.2f} leva needed.")