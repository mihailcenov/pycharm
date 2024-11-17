number_easter_breads = int(input())
best_chef = ""
max_points = 0
for _ in range(number_easter_breads):
    name_of_chef = input()
    total_points = 0
    while True:
        score = input()
        if score == "Stop":
            break
        total_points += int(score)
    print(f"{name_of_chef} has {total_points} points.")
    if total_points > max_points:
        max_points = total_points
        best_chef = name_of_chef
        print(f"{name_of_chef} is the new number 1!")

print(f"{best_chef} won competition with {max_points} points!")




