initial_eggs = int(input())
eggs_in_the_shop = initial_eggs
total_sold = 0
while True:
    command = input()

    if command == "Closed":
        print(f"Store is closed!")
        print(f"{total_sold} eggs sold.")
        break

    eggs_count = int(input())

    if command == "Buy":
        if eggs_count > eggs_in_the_shop:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_the_shop}.")
            break
        else:
            eggs_in_the_shop -= eggs_count
            total_sold = total_sold + eggs_count
    elif command == "Fill":
        eggs_in_the_shop += eggs_count



