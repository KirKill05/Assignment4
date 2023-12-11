class Movie:
    def __init__(self, year, name, genre):
        self.year = year
        self.name = name
        self.genre = genre

class MovieManager:
    def __init__(self):
        self.movies_by_year = {}

    def create_movie(self, year, name, genre):
        if year not in self.movies_by_year:
            self.movies_by_year[year] = []

        movie = Movie(year, name, genre)
        self.movies_by_year[year].append(movie)
        print(f"Movie '{name}' added successfully.")

    def read_movie(self, key_attribute, non_key_attribute):
        for year, movies in self.movies_by_year.items():
            for movie in movies:
                if str(getattr(movie, key_attribute)) == non_key_attribute or \
                        getattr(movie, key_attribute) == non_key_attribute:
                    print(f"Year: {movie.year}, Name: {movie.name}, Genre: {movie.genre}")

    def edit_movie(self, year, search_name, new_name, new_genre):
        if year in self.movies_by_year:
            for movie in self.movies_by_year[year]:
                if movie.name == search_name:
                    movie.name = new_name
                    movie.genre = new_genre
                    print(f"Movie edited successfully.")
                    return
            print(f"Movie with the given name not found for editing.")
        else:
            print(f"No movies found for the given year.")

    def delete_movie(self, year):
        if year in self.movies_by_year:
            del self.movies_by_year[year]
            print(f"All movies for the year {year} deleted successfully.")
        else:
            print(f"No movies found for the given year.")