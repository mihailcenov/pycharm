import math
price_tennis_racket = float(input())
number_tennis_rackets = int(input())
number_shoes = int(input())

total_price_rackets = price_tennis_racket * number_tennis_rackets
price_shoes = price_tennis_racket / 6
total_price_shoes = number_shoes * price_shoes
extra_items = (total_price_rackets + total_price_shoes) * 0.20
all_things_price = total_price_rackets + total_price_shoes + extra_items
things_paid_by_player = all_things_price / 8
things_paid_by_boses = (all_things_price * 7) / 8
print(f"Price to be paid by Djokovic {math.floor(things_paid_by_player)}")
print(f"Price to be paid by sponsors {math.ceil(things_paid_by_boses)}")