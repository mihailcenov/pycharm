screening = input()
movie_package = input()
number_of_tickets = int(input())
price = 0
if screening == "John Wick":
    if movie_package == "Drink":
        price = 12
    elif movie_package == "Popcorn":
        price = 15
    elif movie_package == "Menu":
        price = 19
elif screening == "Star Wars":
    if movie_package == "Drink":
        price = 18
    elif movie_package == "Popcorn":
        price = 25
    elif movie_package == "Menu":
        price = 30
elif screening == "Jumanji":
    if movie_package == "Drink":
        price = 9
    elif movie_package == "Popcorn":
        price = 11
    elif movie_package == "Menu":
        price = 14

if screening == "Star Wars" and number_of_tickets >= 4:
    price -= price * 0.30

if screening == "Jumanji" and number_of_tickets == 2:
    price -= price * 0.15

total_price = price * number_of_tickets
print(f"Your bill is {total_price:.2f} leva.")



