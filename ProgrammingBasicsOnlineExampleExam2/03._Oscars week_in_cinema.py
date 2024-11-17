movie_name = input()#("A Star Is Born", "Bohemian Rhapsody","Green Book" или "The Favourite")
type_room = input() # normal", "luxury" или "ultra luxury
bought_tickets = int(input())
price = 0

if movie_name == "A Star Is Born":
    if type_room == "normal":
        price = 7.50
    elif type_room == "luxury":
        price = 10.50
    elif type_room == "ultra luxury":
        price = 13.50
elif movie_name == "Bohemian Rhapsody":
    if type_room == "normal":
        price = 7.35
    elif type_room == "luxury":
        price = 9.45
    elif type_room == "ultra luxury":
        price = 12.75
elif movie_name == "Green Book":
    if type_room == "normal":
        price = 8.15
    elif type_room == "luxury":
        price = 10.25
    elif type_room == "ultra luxury":
        price = 13.25
elif movie_name == "The Favourite":
    if type_room == "normal":
        price = 8.75
    elif type_room == "luxury":
        price = 11.55
    elif type_room == "ultra luxury":
        price = 13.95

total_price = price * bought_tickets
print(f"{movie_name} -> {total_price:.2f} lv.")




