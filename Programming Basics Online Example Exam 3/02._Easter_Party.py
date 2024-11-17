number_guests = int(input())
price_per_person = float(input())
desi_budget = float(input())

if 10 <= number_guests <= 15:
    price_per_person -= price_per_person * 0.15
elif 15 < number_guests <= 20:
    price_per_person -= price_per_person * 0.20
elif number_guests > 20:
    price_per_person -= price_per_person * 0.25
else:
    price_per_person = price_per_person

#print(f"{price_per_person}")
cake = desi_budget * 0.10
# print(cake)
total_price = cake + (number_guests * price_per_person)
# print(f"{total_price}")
if total_price > desi_budget:
    needed_money = total_price - desi_budget
    print(f"No party! {needed_money:.2f} leva needed.")
else:
    left_money = desi_budget - total_price
    print(f"It is party time! {left_money:.2f} leva left.")