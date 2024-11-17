import math
number_days = int(input())
left_food_in_kilos = int(input())
dog_food_per_day_kilos = float(input())
cat_food_per_day_kilos = float(input())
turtle_food_in_grams = float(input()) / 1000

needed_dog_food = number_days * dog_food_per_day_kilos
needed_cat_food = number_days * cat_food_per_day_kilos
needed_turtle_food = number_days * turtle_food_in_grams

total_food = needed_dog_food + needed_cat_food + needed_turtle_food

if total_food < left_food_in_kilos:
    enough_food = left_food_in_kilos - total_food
    print(f"{math.floor(enough_food)} kilos of food left.")
else:
    not_enough_food = total_food - left_food_in_kilos
    print(f"{math.ceil(not_enough_food)} more kilos of food are needed.")