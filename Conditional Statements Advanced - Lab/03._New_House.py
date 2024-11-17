# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.

# Роза	 Далия	Лале	Нарцис	Гладиола
# 5	      3.80	     2.80	    3	  2.50
# Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";?
# "Not enough money, you need {нужната сума} leva more.".

type_flowers = input()
number_flowers = int(input())
budget = int(input())
price = 0
discount = 0

if type_flowers == "Roses":
    price = 5.00
    if number_flowers > 80:
        discount = 0.10
elif type_flowers == "Dahlias":
    price = 3.80
    if number_flowers > 90:
        discount = 0.15
elif type_flowers == "Tulips":
    price = 2.80
    if number_flowers > 80:
        discount = 0.15
elif type_flowers == "Narcissus":
    price = 3.00
    if number_flowers < 120:
        discount = - 0.15
elif type_flowers == "Gladiolus":
    price = 2.50
    if number_flowers < 80:
        discount = - 0.20


total_price = price * number_flowers * (1 - discount)

if budget >= total_price:
    money = budget - total_price

    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {money :.2f} leva left.")

else:
    money_needed = total_price - budget
    print(f"Not enough money, you need {money_needed :.2f} leva more.")









