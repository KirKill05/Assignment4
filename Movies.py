class Movie:
    def __init__(self, year, name, genre):
        self.year = year
        self.name = name
        self.genre = genre

class MovieManager:
    def __init__(self):
        self.movies = []

    def create_movie(self, year, name, genre):
        movie = Movie(year, name, genre)
        self.movies.append(movie)
        print(f"Movie '{name}' added successfully.")

    def read_movie(self, key_attribute, non_key_attribute):
        for movie in self.movies:
            if str(getattr(movie, key_attribute)) == non_key_attribute or \
                    getattr(movie, key_attribute) == non_key_attribute:
                print(f"Year: {movie.year}, Name: {movie.name}, Genre: {movie.genre}")

    def edit_movie(self, year, new_name, new_genre):
        for movie in self.movies:
            if movie.year == year:
                movie.name = new_name
                movie.genre = new_genre
                print(f"Movie edited successfully.")

    def delete_movie(self, year):
        for movie in self.movies:
            if movie.year == year:
                self.movies.remove(movie)
                print(f"Movie deleted successfully.")
                break