#"Bansko",  "Borovets", "Varna" или "Burgas")
#noEquipment",  "withEquipment", "noBreakfast" или "withBreakfast")
# 3.	Притежание на VIP отстъпка - текст с възможности  "yes" или "no"


city_name = input()
type_of_package = input()
vip_discount = input()
days_to_stay = int(input())

price = 0
valid_cities = ("Bansko", "Borovets", "Varna", "Burgas")
valid_vip_discount = ("yes", "no")
valid_type_of_package = ("noEquipment", "withEquipment", "noBreakfast", "withBreakfast")

if days_to_stay <= 0:
    print(f"Days must be positive number!")
else:
    if (city_name not in valid_cities) or (vip_discount not in valid_vip_discount) or\
            (type_of_package not in valid_type_of_package):  # tuple
        print("Invalid input!")
    else:
        if days_to_stay > 7:
            days_to_stay -= 1
        if city_name == "Bansko" or city_name == "Borovets":
            if type_of_package == "noEquipment":
                price = 80
                if vip_discount == "yes":
                    price -= (price * 5) / 100
            elif type_of_package == "withEquipment":
                price = 100
                if vip_discount == "yes":
                    price -= (price * 10) / 100
        elif city_name == "Varna" or city_name == "Burgas":
            if type_of_package == "noBreakfast":
                price = 100
                if vip_discount == "yes":
                    price -= (price * 7) / 100
            elif type_of_package == "withBreakfast":
                price = 130
                if vip_discount == "yes":
                    price -= (price * 12) / 100

        total_price = price * days_to_stay
        print(f"The price is {total_price:.2f}lv! Have a nice time!")
