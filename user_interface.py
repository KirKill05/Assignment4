class UserInterface:
    def show_menu(self):
        print("1. Add Movie")
        print("2. Search Movie")
        print("3. Edit Movie")
        print("4. Delete Movie")
        print("5. Exit")

    def get_user_choice(self):
        while True:
            try:
                return int(self.get_user_input("Enter your choice: "))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_user_input(self, prompt):
        return input(prompt) 