import math
number_guests = int(input())
budget = int(input())
# Един козунак струва 4лв.
# Едно яйце струва 0.45лв.
# Известно е, че един козунак стига за трима човека, като всеки гост ще получи и по 2 яйца
# . Вашата задача е да намерите колко козунака и яйца трябва да купи

number_bread = math.ceil(number_guests / 3)
number_eggs = number_guests * 2
total_products = (number_bread * 4) + (number_eggs * 0.45)
#print(total_products)
if budget >= total_products:
    left_money = budget- total_products
    print(f"Lyubo bought {number_bread} Easter bread and {number_eggs} eggs.")
    print(f"He has {left_money:.2f} lv. left.")
else:
    needed_money = total_products - budget
    print(f"Lyubo doesn't have enough money.")
    print(f"He needs {needed_money:.2f} lv. more.")
