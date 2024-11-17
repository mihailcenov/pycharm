n = int(input())
previous_pair_sum = None  # Променлива за предишната стойност на двойката
max_difference = 0  # Променлива за максималната разлика
equal_pairs = True  # Флаг, който указва дали всички двойки имат еднаква стойност
#previous_pair_sum = 0
for i in range(n):
    first_number = int(input())
    second_number = int(input())
    # Изчисляваме сумата на текущата двойка
    current_pair_sum = first_number + second_number
    if previous_pair_sum is not None:
        # Изчисляваме разликата между текущата и предишната двойка
        difference = abs(current_pair_sum - previous_pair_sum)
        if difference > max_difference:
            max_difference = difference
            # Ако стойностите на двойките са различни, задаваме флага на False
        if current_pair_sum != previous_pair_sum:
                equal_pairs = False

    # Обновяваме стойността на предишната двойка
    previous_pair_sum = current_pair_sum

if equal_pairs:
    print(f"Yes, value={previous_pair_sum}")
else:
    print(f"No, maxdiff={max_difference}")


