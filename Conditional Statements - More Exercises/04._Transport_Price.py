kilometres = int(input())
day_time = input()

total_price = 0.0
if kilometres < 20:
    if day_time == "day":
        total_price = 0.70 + kilometres * 0.79
    else:
        total_price = 0.70 + kilometres * 0.90
elif 20 <= kilometres < 100:
        total_price = kilometres * 0.09
else:
        total_price = kilometres * 0.06


print(f"{total_price:.2f}")



