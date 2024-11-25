sold_games = int(input())
percent_count_hearthne = 0
percent_fornite = 0
percent_overwatch = 0
percent_others = 0
# •	•	Hearthstone
# # •	Fornite
# # •	Overwatch
# # •	Others
for _ in range(sold_games):
    games_name = input()
    if games_name == "Hearthstone":
        percent_count_hearthne += 1
    elif games_name == "Fornite":
        percent_fornite += 1
    elif games_name == "Overwatch":
        percent_overwatch += 1
    else:
        percent_others += 1

total_percent_hearthstone = (percent_count_hearthne / sold_games) * 100
total_percent_fornite = (percent_fornite / sold_games) * 100
total_percent_overwatch = (percent_overwatch / sold_games) * 100
total_percent_others = (percent_others / sold_games) * 100

print(f"Hearthstone - {total_percent_hearthstone:.2f}%")
print(f"Fornite - {total_percent_fornite:.2f}%")
print(f"Overwatch - {total_percent_overwatch:.2f}%")
print(f"Others - {total_percent_others:.2f}%")




