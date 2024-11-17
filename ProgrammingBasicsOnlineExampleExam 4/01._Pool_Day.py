import math
number_people = int(input())
entrance_tax = float(input())
lounge_chair_price = float(input())
umbrella_price = float(input())

price_for_people = number_people * entrance_tax
people_with_lounge_chair_count = (math.ceil(number_people * 0.75))
price_for_people_with_lounge_chair = people_with_lounge_chair_count * lounge_chair_price
people_with_umbrella_count = (math.ceil(number_people * 0.50))
price_for_people_with_umbrella_count = people_with_umbrella_count * umbrella_price

total_price = price_for_people + price_for_people_with_lounge_chair + price_for_people_with_umbrella_count
print(f"{total_price:.2f} lv.")

