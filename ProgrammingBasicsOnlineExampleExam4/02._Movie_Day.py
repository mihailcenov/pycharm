import math

time_for_photos = int(input())
number_scenes = int(input())
duration_for_one_scene = int(input())

time_for_ground_preparation = (time_for_photos * 15) / 100
time_for_scenes = number_scenes * duration_for_one_scene + time_for_ground_preparation

if time_for_photos < time_for_scenes:
    needed_time = time_for_scenes - time_for_photos
    print(f"Time is up! To complete the movie you need {round(needed_time)} minutes.")
else:
    left_time = time_for_photos - time_for_scenes
    print(f"You managed to finish the movie on time! You have {round(left_time)} minutes left!")