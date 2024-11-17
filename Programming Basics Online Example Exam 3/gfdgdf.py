# Входни данни
initial_eggs = int(input())
eggs_in_store = initial_eggs
total_sold = 0

# Започваме цикъл за обработка на командите
while True:
    command = input()

    # Проверка за край на програмата
    if command == "Close":
        print("Store is closed!")
        print(f"{total_sold} eggs sold.")
        break

    # Брой яйца за купуване или допълване
    eggs_count = int(input())

    if command == "Buy":
        # Проверка дали има достатъчно яйца за купуване
        if eggs_count > eggs_in_store:
            print("Not enough eggs in store!")
            print(f"You can buy only {eggs_in_store}.")
            break
        else:
            eggs_in_store -= eggs_count
            total_sold += eggs_count

    elif command == "Fill":
        # Допълване на яйцата в магазина
        eggs_in_store += eggs_count
