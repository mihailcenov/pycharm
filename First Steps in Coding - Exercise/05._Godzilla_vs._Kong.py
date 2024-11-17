budget_film = float(input())
number_actors = int(input())
clothes_for_one_actor = float(input())

decor = budget_film * 0.10

total_price_for_actors_clothes = number_actors * clothes_for_one_actor

if number_actors > 150:
    total_price_for_actors_clothes *= 0.90

total_cost = decor + total_price_for_actors_clothes
if budget_film >= total_cost:
    money_left = budget_film - total_cost
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_needed = total_cost - budget_film
    print("Not enough money!" )
    print(f"Wingard needs {money_needed:.2f} leva more.")










