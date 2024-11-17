import math

movie_name = input()
number_seasons = int(input())
number_episodes = int(input())
time_episodes = float(input())

time_for_ads = time_episodes * 0.20
total_time_for_episode = time_for_ads + time_episodes
extra_episode = number_seasons * 10
total_time = number_episodes * total_time_for_episode * number_seasons + extra_episode
print(f"Total time needed to watch the {movie_name} series is {math.floor(total_time)} minutes.")