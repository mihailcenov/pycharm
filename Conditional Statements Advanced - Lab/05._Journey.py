budget = float(input())
season = input()
# "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# •	"{Вид почивка} - {Похарчена сума}":
destination = ""
vacation_place = ""
vacation_price = 0.0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        vacation_price = budget * 0.30
        vacation_place = "Camp"
    elif season == "winter":
        vacation_price = budget * 0.70
        vacation_place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        vacation_price = budget * 0.40
        vacation_place = "Camp"
    elif season == "winter":
        vacation_price = budget * 0.80
        vacation_place = "Hotel"
else:
    destination = "Europe"
    vacation_price = budget * 0.90
    vacation_place = "Hotel"


print(f"Somewhere in {destination}")
print(f"{vacation_place} - {vacation_price:.2f}")