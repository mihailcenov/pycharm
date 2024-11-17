budget = float(input())
numbers_movies = int(input())
price_per_movie = 0.0
total_cost = 0.0

movies_with_discount = {
    "Thrones": 0.5,
    "Lucifer": 0.4,
    "Protector": 0.3,
    "TotalDrama": 0.2,
    "Area": 0.1,
    "Teen Wolf": 0.9
}

# for test

# for key, value in movies_with_discount.items():
#     print(f"Key: {key}, Value: {value}")

for _ in range(numbers_movies):
    movie_name = input()
    price_per_movie = float(input())

    if movie_name in movies_with_discount:
        price_per_movie -= price_per_movie * movies_with_discount[movie_name]
    total_cost += price_per_movie

if budget >= total_cost:
    left_money = budget - total_cost
    print(f"You bought all the series and left with {left_money:.2f} lv.")
else:
    needed_money = total_cost -budget
    print(f"You need {needed_money:.2f} lv. more to buy the series!")

