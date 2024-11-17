world_recotd_in_seconds = float(input())
distance_in_meters = float(input())
distance_in_seconds_for_one_meter = float(input())

his_distance_in_seconds = distance_in_meters * distance_in_seconds_for_one_meter
back_in_seconds = distance_in_meters // 15
added_seconds = back_in_seconds * 12.5
total_time = his_distance_in_seconds + added_seconds
if total_time < world_recotd_in_seconds:
    #first_try = total_time - world_recotd_in_seconds
   # print(first_try)
    #print(f"No, he failed! He was {first_try :.2f} seconds slower.")
    print(f"Yes, he succeeded! The new world record is {total_time :.2f} seconds.")
else:
    difference = total_time - world_recotd_in_seconds
    print(f"No, he failed! He was {difference :.2f} seconds slower.")










