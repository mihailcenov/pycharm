stadium_capacity = int(input())
total_fans = int(input())
fans_A = 0
fans_B = 0
fans_V = 0
fans_G = 0

for _ in range(total_fans):
    sector = input()
    if sector == "A":
        fans_A += 1
    elif sector == "B":
        fans_B += 1
    elif sector == "V":
        fans_V += 1
    elif sector == "G":
        fans_G += 1

percent_A = (fans_A / total_fans) * 100
percent_B = (fans_B / total_fans) * 100
percent_V = (fans_V / total_fans) * 100
percent_G = (fans_G / total_fans) * 100

total_percent = (total_fans / stadium_capacity) * 100

print(f"{percent_A:.2f}%")
print(f"{percent_B:.2f}%")
print(f"{percent_V:.2f}%")
print(f"{percent_G:.2f}%")
print(f"{total_percent:.2f}%")