total_games = 0
win_games = 0
loss_games = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break

    num_games = int(input())
    for game in range(1, num_games + 1):
        desi_team_points = int(input())
        opponent_team_points = int(input())

        total_games += 1
        if desi_team_points > opponent_team_points:
            win_games += 1
            difference = desi_team_points - opponent_team_points
            print(f"Game {game} of tournament {tournament_name}: win with {difference} points.")
        else:
            loss_games += 1
            difference = opponent_team_points - desi_team_points
            print(f"Game {game} of tournament {tournament_name}: lost with {difference} points.")

win_percentage = (win_games / total_games) * 100
loss_percentage = (loss_games / total_games) * 100

print(f"{win_percentage:.2f}% matches win")
print(f"{loss_percentage:.2f}% matches lost")