movie_name = input()
number_days = int(input())
number_tickets = int(input())
price_per_ticket = float(input())
sinema_percent = int(input())

total_price_for_tickets = number_tickets * price_per_ticket
profit_for_the_whole_period = number_days * total_price_for_tickets
profit_for_the_sinema = (profit_for_the_whole_period * sinema_percent) / 100
profit_for_softuni = profit_for_the_whole_period - profit_for_the_sinema

print(f"The profit from the movie {movie_name} is {profit_for_softuni:.2f} lv.")