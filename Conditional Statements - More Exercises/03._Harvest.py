#
#
import math
square_meters_yard = int(input())
grapes_for_one_meters = float(input())
needed_liters_wine = int(input())
number_workers = int(input())

total_grapes = square_meters_yard * grapes_for_one_meters
wine = (total_grapes * 40 / 100) / 2.5

if wine < needed_liters_wine:
    left_wine = needed_liters_wine - wine
    print(f"It will be a tough winter! More {math.floor(left_wine)} liters wine needed.")

else:
        wine_for_workers = wine - needed_liters_wine
        left_wine_for_workers = wine_for_workers / number_workers
        print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
        print(f"{math.ceil(wine_for_workers)} liters left -> {math.ceil(left_wine_for_workers)} liters per person.")
