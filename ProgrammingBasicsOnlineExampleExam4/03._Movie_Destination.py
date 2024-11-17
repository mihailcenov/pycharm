budget_film = float(input())
destination = input()
year_season = input()
number_of_days = int(input())
price = 0.0
if destination == "Dubai":
    if year_season == "Summer":
        price = 40000
    elif year_season == "Winter":
        price = 45000
elif destination == "Sofia":
    if year_season == "Summer":
        price = 12500
    elif year_season == "Winter":
        price = 17000
elif destination == "London":
    if year_season == "Summer":
        price = 20250
    elif year_season == "Winter":
        price = 24000

total_price = price * number_of_days

if destination == "Dubai":
    total_price -= total_price * 0.30
if destination == "Sofia":
    total_price += total_price * 0.25
else:
    total_price = total_price

if total_price > budget_film:
    needed_money = total_price - budget_film
    print(f"The director needs {needed_money:.2f} leva more!")
else:
    left_money = budget_film - total_price
    print(f"The budget for the movie is enough! We have {left_money:.2f} leva left!")





