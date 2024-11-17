
volume_pool = int(input())
debit_per_hour_first_tube = int(input())
debit_per_hour_second_tube = int(input())
worker_hours_been_away = float(input())
# За 3 часа:
liters_first_tube = debit_per_hour_first_tube * worker_hours_been_away
liters_second_tube = debit_per_hour_second_tube * worker_hours_been_away
total_water = liters_first_tube + liters_second_tube
percent_water_in_pool = (total_water / volume_pool) * 100

percent_first_tube = (liters_first_tube / total_water) * 100
percent_second_tube = (liters_second_tube / total_water) * 100

