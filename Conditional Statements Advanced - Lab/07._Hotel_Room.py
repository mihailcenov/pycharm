# •	На първия ред е месецът - May, June, July, August, September или October;
# •

# another way

# and then use MONTHS[0], MONTHS[1] .... MONTH[11]

month = input()  #May, June, July, August, September или October; Apartment Studio
number_nights = int(input())
#room_type = ""
#price_per_night = 0.0
discount = 0.0
price_apartament = 0.0
price_studio = 0.0
app_discount = 0.0
if month == "May" or month == "October":
    price_apartament = number_nights * 65
    price_studio = number_nights * 50
    if number_nights > 14:
        discount = price_studio * 0.30
    elif number_nights > 7:
        discount = price_studio * 0.05
elif month == "June" or month == "September":
    price_apartament = number_nights * 68.70
    price_studio = number_nights * 75.20
    if number_nights > 14:
        discount = price_studio * 0.20
elif month == "July" or month == "August":
    price_apartament = number_nights * 77
    price_studio = number_nights * 76

if number_nights > 14:
    app_discount = price_apartament * 0.10

total_money_studio = price_studio - discount
total_money_apartament = price_apartament - app_discount
print(f"Apartment: {total_money_apartament:.2f} lv.")
print(f"Studio: {total_money_studio:.2f} lv.")


