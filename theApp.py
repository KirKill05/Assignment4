from DataPersistance import * 
from user_interface import *

class MovieApp:
    def __init__(self):
        self.ui = UserInterface()
        self.movie_manager = MovieManager()
        self.data_persistence_manager = DataPersistenceManager()

    def run(self):
        self.movie_manager.movies = self.data_persistence_manager.load_data()

        while True:
            try:
                self.ui.show_menu()
                choice = self.ui.get_user_choice()

                if choice == 1:
                    year = int(self.ui.get_user_input("Enter the year: "))
                    name = self.ui.get_user_input("Enter the name: ")
                    genre = self.ui.get_user_input("Enter the genre: ")
                    self.movie_manager.create_movie(year, name, genre)

                elif choice == 2:
                    key_attribute = "year"
                    non_key_attribute = self.ui.get_user_input("Enter the year or name to search: ")
                    self.movie_manager.read_movie(key_attribute, non_key_attribute)

                elif choice == 3:
                    year = int(self.ui.get_user_input("Enter the year of the movie to edit: "))
                    new_name = self.ui.get_user_input("Enter the new name: ")
                    new_genre = self.ui.get_user_input("Enter the new genre: ")
                    self.movie_manager.edit_movie(year, new_name, new_genre)

                elif choice == 4:
                    year = int(self.ui.get_user_input("Enter the year of the movie to delete: "))
                    self.movie_manager.delete_movie(year)

                elif choice == 5:
                    # Exit and save data
                    self.data_persistence_manager.save_data(self.movie_manager.movies)
                    print("Exiting the program.")
                    break

            except Exception as e:
                print(f"An error occurred: {e}")
    
app = MovieApp()
app.run()