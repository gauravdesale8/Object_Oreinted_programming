class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

my_fav_movie = Movie("Iron Man", 2008, "English", 8.5)
your_fav_movie = Movie("Flash", 2023, "English", 8.4)

print("")
print("<><><><><><><><><><><><><>")
print(" MY FAVOURITE MOVIE")
print(my_fav_movie.title)
print(my_fav_movie.year)
print(my_fav_movie.language)
print(my_fav_movie.rating)
print("<><><><><><><><><><><><><>")

print("")
print("<><><><><><><><><><><><><>")
print(" YOUR FAVOURITE MOVIE")
print(your_fav_movie.title)
print(your_fav_movie.year)
print(your_fav_movie.language)
print(your_fav_movie.rating)
print("<><><><><><><><><><><><><>")
print("")