import math
number_games = int(input())
start_points = int(input())
points_earned = 0
wins = 0


for _ in range(number_games):
    stage_in_the_tournament = input()
    if stage_in_the_tournament == "W":
        points_earned += 2000
        wins += 1
    elif stage_in_the_tournament == "F":
        points_earned += 1200
    elif stage_in_the_tournament == "SF":
        points_earned += 720

final_points = start_points + points_earned
average_points = points_earned / number_games
win_percentage = (wins / number_games) * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{win_percentage:.2f}%")
