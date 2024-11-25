team_name = input()
number_played_games = int(input())
points_gained = 0
total_points = 0
won_games = 0
draw_games = 0
lost_games = 0
for _ in range(number_played_games):
    command = input()
    if command == "W":
        points_gained += 3
        won_games += 1
    elif command == "D":
        points_gained += 1
        draw_games += 1
    elif command == "L":
        points_gained = points_gained
        lost_games += 1

if number_played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    total_points += points_gained
    percent_wins = (won_games / number_played_games) * 100

    print(f"{team_name} has won {total_points} points during this season.")
    print("Total stats:")
    print(f"## W: {won_games}")
    print(f"## D: {draw_games}")
    print(f"## L: {lost_games}")
    print(f"Win rate: {percent_wins:.2f}%")

