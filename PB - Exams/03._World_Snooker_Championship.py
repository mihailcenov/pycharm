stage_of_the_championship = input()
ticket_type = input()
number_tickets = int(input())
pictures = input()
price = 0.0
discount = 0.0
photo = 40.0

if stage_of_the_championship == "Quarter final":
    if ticket_type == "Standard":
        price = 55.50
    elif ticket_type == "Premium":
        price = 105.20
    elif ticket_type == "VIP":
        price = 118.90
elif stage_of_the_championship == "Semi final":
    if ticket_type == "Standard":
        price = 75.88
    elif ticket_type == "Premium":
        price = 125.22
    elif ticket_type == "VIP":
        price = 300.40
elif stage_of_the_championship == "Final":
    if ticket_type == "Standard":
        price = 110.10
    elif ticket_type == "Premium":
        price = 160.66
    elif ticket_type == "VIP":
        price = 400

total_price = price * number_tickets
photo = number_tickets * 40
if total_price > 4000:
    discount = total_price - (total_price * 25) / 100

elif total_price > 2500:
    discount = total_price - (total_price * 10) / 100


if pictures == 'Y':
    if total_price > 4000:
        discount = total_price - (total_price * 25) / 100
        print(f"{discount:.2f}")
    elif total_price > 2500:
        discount = total_price - (total_price * 10) / 100
        print(f"{discount + photo:.2f}")
    else:
        print(f"{total_price + photo:.2f}")
elif pictures == 'N':
    if total_price > 4000:
        print(f"{discount:.2f}")
    elif total_price > 2500:
        print(f"{discount:.2f}")
    else:
        print(f"{total_price:.2f}")










