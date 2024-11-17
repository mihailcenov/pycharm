number_months = int(input())
electricity_bills = 0
water = 20
internet = 15
total_electricity = 0
total_water = 0
total_internet = 0
for _ in range(1, number_months + 1, 1):
    electricity_bills = float(input())
    total_electricity += electricity_bills

total_water = water * number_months
total_internet = number_months * internet
total_bills = total_electricity + total_water + total_internet
month1 = (total_water + total_internet + total_electricity) * 1.2
average_bill = (total_water + total_internet + total_electricity + month1) / number_months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {month1:.2f} lv")
print(f"Average: {average_bill:.2f} lv")