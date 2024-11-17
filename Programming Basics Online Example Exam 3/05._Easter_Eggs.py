number_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

for _ in range(number_eggs):
    eggs_paint = input()
    if eggs_paint == "red":
        red_eggs += 1
    elif eggs_paint == "orange":
        orange_eggs += 1
    elif eggs_paint == "blue":
        blue_eggs += 1
    elif eggs_paint == "green":
        green_eggs += 1

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")

max_count = max(red_eggs, orange_eggs, blue_eggs, green_eggs)
if max_count == red_eggs:
    max_color = "red"
elif max_count == orange_eggs:
    max_color = "orange"
elif max_count == blue_eggs:
    max_color = "blue"
else:
    max_color = "green"

print(f"Max eggs: {max_count} -> {max_color}")