budget = float(input())
numbers_movies = int(input())
price_per_movie = 0.0
total_cost = 0.0


for _ in range(numbers_movies):
    movie_name = input()
    price_per_movie = float(input())
    if movie_name == "Thrones":
        price_per_movie -= price_per_movie * 0.50
    elif movie_name == "Lucifer":
        price_per_movie -= price_per_movie * 0.40
    elif movie_name == "Protector":
        price_per_movie -= price_per_movie * 0.30
    elif movie_name == "TotalDrama":
        price_per_movie -= price_per_movie * 0.20
    elif movie_name == "Area":
        price_per_movie -= price_per_movie * 0.10
    else:
        price_per_movie = price_per_movie

    total_cost += price_per_movie
# print(f"{total_cost}")
# print(f"{price_per_movie}")
if budget >= total_cost:
    left_money = budget - total_cost
    print(f"You bought all the series and left with {left_money:.2f} lv.")
else:
    needed_money = total_cost - budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")

