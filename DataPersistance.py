import json
from Movies import *
class DataPersistenceManager:
    def __init__(self, filename='movies.json'):
        self.filename = filename

    def save_data(self, movies):
        try:
            with open(self.filename, 'w') as file:
                json.dump([vars(movie) for movie in movies], file)
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                return [Movie(movie['year'], movie['name'], movie['genre']) for movie in data]
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Error loading data: {e}")
            return []