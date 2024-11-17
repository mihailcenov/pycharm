# Дефинираме цените на продуктите
prices = {
    "basket": 1.50,
    "wreath": 3.80,
    "chocolate bunny": 7.00
}

# Въвеждаме броя на клиентите
num_clients = int(input())
total_sum = 0

# Обхождаме всеки клиент
for _ in range(num_clients):
    items_count = 0
    client_sum = 0

    # Четем покупките за всеки клиент до команда "Finish"
    while True:
        purchase = input()
        if purchase == "Finish":
            break
        client_sum += prices[purchase]
        items_count += 1

    # Проверка за четен брой продукти и прилагане на отстъпка
    if items_count % 2 == 0:
        client_sum *= 0.80  # Прилагаме 20% отстъпка

    # Показваме сумата за текущия клиент
    print(f"You purchased {items_count} items for {client_sum:.2f} leva.")

    # Добавяме сумата към общата за всички клиенти
    total_sum += client_sum

# Изчисляваме и показваме средната сума на клиент
average_bill = total_sum / num_clients
print(f"Average bill per client is: {average_bill:.2f} leva.")
