number_people_in_the_gym = int(input())
person_back = 0
person_chest = 0
person_legs = 0
person_abs = 0
person_drink_shake = 0
person_eat_bar = 0
for _ in range(number_people_in_the_gym):
    activity_in_the_gym = input() #Chest", "Legs", "Abs", "Protein shake" или "Protein bar")
    if activity_in_the_gym == "Back":
        person_back += 1
    elif activity_in_the_gym == "Chest":
        person_chest += 1
    elif activity_in_the_gym == "Legs":
        person_legs += 1
    elif activity_in_the_gym == "Abs":
        person_abs += 1
    elif activity_in_the_gym == "Protein shake":
        person_drink_shake += 1
    elif activity_in_the_gym == "Protein bar":
        person_eat_bar += 1

print(f'{person_back} - back')
print(f"{person_chest} - chest")
print(f"{person_legs} - legs")
print(f"{person_abs} - abs")
print(f"{person_drink_shake} - protein shake")
print(f"{person_eat_bar} - protein bar")
work_out = person_back + person_chest + person_legs + person_abs
bought_products = person_drink_shake + person_eat_bar
all_work_out = (work_out / number_people_in_the_gym) * 100
all_people_bought_products = (bought_products / number_people_in_the_gym) * 100

print(f"{all_work_out:.2f}% - work out")
print(f"{all_people_bought_products:.2f}% - protein")