number_people_in_the_game = int(input())
numbers_for_each_move = 0
result = 0
count_0_9 = 0
count_10_19 = 0
count_20_29 = 0
count_30_39 = 0
count_40_50 = 0
count_invalid = 0
for _ in range(number_people_in_the_game):
    numbers_for_each_move = int(input())
    if 0 <= numbers_for_each_move <= 9:
        result += (numbers_for_each_move * 20) / 100
        count_0_9 += 1
    elif 10 <= numbers_for_each_move <= 19:
        result += (numbers_for_each_move * 30) / 100
        count_10_19 += 1
    elif 20 <= numbers_for_each_move <= 29:
        result += (numbers_for_each_move * 40) / 100
        count_20_29 += 1
    elif 30 <= numbers_for_each_move <= 39:
        result += 50
        count_30_39 += 1
    elif 40 <= numbers_for_each_move <= 50:
        result += 100
        count_40_50 += 1
    elif numbers_for_each_move < 0 or numbers_for_each_move > 50:
        result = result / 2
        count_invalid += 1

#print(result)
total_moves = number_people_in_the_game
percent_0_9 = (count_0_9 / total_moves) * 100
percent_10_19 = (count_10_19 / total_moves) * 100
percent_20_29 = (count_20_29 / total_moves) * 100
percent_30_39 = (count_30_39 / total_moves) * 100
percent_40_50 = (count_40_50 / total_moves) * 100
percent_invalid = (count_invalid / total_moves) * 100

print(f"{result:.2f}")
print(f"From 0 to 9: {percent_0_9:.2f}%")
print(f"From 10 to 19: {percent_10_19:.2f}%")
print(f"From 20 to 29: {percent_20_29:.2f}%")
print(f"From 30 to 39: {percent_30_39:.2f}%")
print(f"From 40 to 50: {percent_40_50:.2f}%")
print(f"Invalid numbers: {percent_invalid:.2f}%")