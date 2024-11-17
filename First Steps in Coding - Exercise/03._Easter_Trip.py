destination = input() #France", "Italy" или "Germany"
dates = input() #21-23", "24-27" или "28-31"
number_nights = int(input())
price = 0.0
if destination == "France":
    if dates == "21-23":
        price = number_nights * 30
    elif dates == "24-27":
        price = number_nights * 35
    elif dates == "28-31":
        price = number_nights * 40
elif destination == "Italy":
    if dates == "21-23":
        price = number_nights * 28
    elif dates == "24-27":
        price = number_nights * 32
    elif dates == "28-31":
        price = number_nights * 39
elif destination == "Germany":
    if dates == "21-23":
        price = number_nights * 32
    elif dates == "24-27":
        price = number_nights * 37
    elif dates == "28-31":
        price = number_nights * 43

print(f"Easter trip to {destination} : {price:.2f} leva.")





