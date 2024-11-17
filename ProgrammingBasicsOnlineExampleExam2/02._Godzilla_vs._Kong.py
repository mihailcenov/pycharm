film_budget = float(input())
number_actors = int(input())
price_clothes_for_one_actor = float(input())


decor = film_budget * 0.10
total_price_for_clothes = number_actors * price_clothes_for_one_actor

if number_actors > 150:
    total_price_for_clothes *= 0.90

total_cost = total_price_for_clothes + decor

if total_cost > film_budget:
    deficit = total_cost - film_budget
    print(f"Not enough money!")
    print(f"Wingard needs {deficit:.2f} leva more.")
else:
    money = film_budget - total_cost
    print(f"Action!")
    print(f"Wingard starts filming with {money:.2f} leva left.")


