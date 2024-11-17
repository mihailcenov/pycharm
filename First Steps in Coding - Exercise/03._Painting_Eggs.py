size_of_eggs = input()  #Large", "Medium" или "Small
colour_of_eggs = input() #Red", "Green" или "Yellow"
number_packets = int(input())
price = 0.0

if size_of_eggs == "Large":
    if colour_of_eggs == "Red":
        price = number_packets * 16
    elif colour_of_eggs == "Green":
        price = number_packets * 12
    elif colour_of_eggs == "Yellow":
        price = number_packets * 9
elif size_of_eggs == "Medium":
    if colour_of_eggs == "Red":
        price = number_packets * 13
    elif colour_of_eggs == "Green":
        price = number_packets * 9
    elif colour_of_eggs == "Yellow":
        price = number_packets * 7
elif size_of_eggs == "Small":
    if colour_of_eggs == "Red":
        price = number_packets * 9
    elif colour_of_eggs == "Green":
        price = number_packets * 8
    elif colour_of_eggs == "Yellow":
        price = number_packets * 5

tax = (price * 35) / 100
total_price = price - tax
print(f"{total_price:.2f} leva.")


