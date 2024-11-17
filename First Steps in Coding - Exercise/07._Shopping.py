# 1.	Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2.	Броят видеокарти - цяло число в интервала [1…100]
# 3.	Броят процесори - цяло число в интервала [1…100]
# 4.	Броят рам памет - цяло число в интервала [1…100]

budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram_memory = int(input())

price_video_cards = number_video_cards * 250
price_processors = price_video_cards * 0.35


total_processors = number_processors * price_processors
price_ram_memory = price_video_cards * 0.10
total_ram_memory = number_ram_memory * price_ram_memory
total_price = price_video_cards + total_processors + total_ram_memory
#print(total_price)
if number_video_cards > number_processors:
    total_price = total_price * 0.85

if total_price <= budget:
    money_left = budget - total_price
    print(f"You have {money_left:.2f} leva left!")

else:
    needed_money = total_price - budget
    print(f"Not enough money! You need {needed_money:.2f} leva more!")


