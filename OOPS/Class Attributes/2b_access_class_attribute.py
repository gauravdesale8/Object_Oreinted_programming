class Movie:
    id_counter = 1

    def __init__(self, title, rating):
        self.id = Movie.id_counter
        self.title = title
        self.rating = rating

        Movie.id_counter += 1


my_movie = Movie("Iron Man", 4.8)
your_movie = Movie("Blue Beetle", 4.5)

print(my_movie.id)
print(your_movie.id)
