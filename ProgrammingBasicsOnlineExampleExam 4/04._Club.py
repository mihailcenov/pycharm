needed_profit = float(input())
price = 0.0
needed_money = 0.0
total_sum = 0.0

while True:
    command = input()
    if command == "Party!":
        needed_money = needed_profit - total_sum
        print(f"We need {needed_money:.2f} leva more.")
        print(f"Club income - {total_sum:.2f} leva.")
        break

    num_cocktails = int(input())
    price = num_cocktails * (len(command))
    if price % 2 == 1:
        price -= (price * 25.0) / 100.0
    total_sum += price
    if total_sum >= needed_profit:
        print(f"Target acquired.")
        print(f"Club income - {total_sum:.2f} leva.")
        break
