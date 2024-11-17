player_name = input()
start_points = 301
successful_shots = 0
unsuccessful_shots = 0
points_scored = 0

while start_points > 0:
    field = input()
    if field != "Retire":
        points_scored = int(input())
    if field == "Single":
        pass
    elif field == "Double":
        points_scored *= 2
    elif field == "Triple":
        points_scored *= 3
    elif field == "Retire":
        print(f"{player_name} retired after {unsuccessful_shots} unsuccessful shots.")
        break

    if start_points >= points_scored:
        #print(f"P1")
        successful_shots += 1
        start_points -= points_scored
        #print(f"start_points left = {start_points}")
        if start_points == 0:
            print(f"{player_name} won the leg with {successful_shots} shots.")
            break
    else:
        #print(f"P2")
        unsuccessful_shots += 1

