import math
name_film = (input())
film_in_minutes = int(input())
break_in_minutes = int(input())

#По време на почивката отделяте време за обяд и време за отдих.
#Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде 1/4 от времето за почивка.
# Време за обяд : 96 * 1/8 = 12.0
# Време за отдих : 96 * 1/4 = 24.0
# Останало време : 96 - 12 - 24 = 60
# Останалото време е по-голямо или равно на продължителността на епизода, следователно печатаме подходящия изход.

time_for_lunch = break_in_minutes / 8
rest_time = break_in_minutes / 4
free_time = break_in_minutes - time_for_lunch - rest_time
#print(free_time)

if free_time >= film_in_minutes:
    total_time = free_time - film_in_minutes
    name_film == "Game of Thrones"
    #print((math.ceil(total_time)))
    print(f"You have enough time to watch {name_film} and left with {(math.ceil(total_time))} minutes free time.")
else:
    name_film =="Teen Wolf"
    needed_time = film_in_minutes - free_time
    #print(math.ceil(needed_time))
    print(f"You don't have enough time to watch {name_film}, you need {(math.ceil(needed_time))} more minutes.")

