
number_rest_days = int(input())
work_days = 365 - number_rest_days
play_during_work_days = work_days * 63
play_during_rest_days = number_rest_days * 127
all_time_for_play = play_during_work_days + play_during_rest_days

diff_hours = 0
diff_minutes = 0
more = False

if all_time_for_play < 30000:
    difference = 30000 - all_time_for_play
    more = False
elif all_time_for_play > 30000:
    difference = all_time_for_play - 30000
    more = True

diff_hours = difference // 60
diff_minutes = difference % 60

if more:
    print(f"Tom will run away")
    print(f"{diff_hours} hours and {diff_minutes} minutes more for play")
else:
    print(f"Tom sleeps well")
    print(f"{diff_hours} hours and {diff_minutes} minutes less for play")

print(f"30000 > 24000 is {30000 > 24000} ")
print(f"30000 < 24000 is {30000 < 24000} ")