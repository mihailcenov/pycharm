# •	На първия ред – броя на групите от катерачи – цяло число в интервала [1...1000]
# •	За всяка една група на отделен ред – броя на хората в групата – цяло число в интервала [1...1000]
numbers_groups = int(input())
number_people_in_group = 0

# •	Група до 5 човека – изкачват Мусала
musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест
#

for _ in range(numbers_groups):
    number_people_in_group = int(input())
    if number_people_in_group <= 5:
        musala = musala + number_people_in_group
    elif 6 <= number_people_in_group <= 12:
        monblan = monblan + number_people_in_group
    elif 13 <= number_people_in_group <= 25:
        kilimanjaro = kilimanjaro + number_people_in_group
    elif 26 <= number_people_in_group <= 40:
        k2 = k2 + number_people_in_group
    else:
        everest = everest + number_people_in_group

all_people = musala + monblan + kilimanjaro + k2 + everest
#print(f"all_people = {all_people}")

percent_musala = (musala / all_people) * 100
percent_monblan = (monblan / all_people) * 100
percent_kilimanjaro = (kilimanjaro / all_people) * 100
percent_k2 = (k2 / all_people) * 100
percent_everest = (everest / all_people) * 100

# print(musala)
# print(monblan)
# print(kilimanjaro)
# print(k2)
# print(everest)
print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")
#

