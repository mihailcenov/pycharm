number_movies = int(input())
highest_rating = float('-inf')
lowest_rating = float('inf')
total_rating = 0
highest_movie = ""
lowest_movie = ""
movie_rating = 0
for _ in range(number_movies):
    movie_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > highest_rating:
        highest_rating = movie_rating
        highest_movie = movie_name
    if movie_rating < lowest_rating :
        lowest_rating = movie_rating
        lowest_movie = movie_name

average_rating = total_rating / number_movies
print(f"{highest_movie} is with highest rating: {highest_rating:.1f}")

print(f"{lowest_movie} is with lowest rating: {lowest_rating:.1f}")

print(f"Average rating: {average_rating:.1f}")
