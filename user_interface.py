class UserInterface:
    def show_menu(self):
        print("1. Add Movie")
        print("2. Search Movie")
        print("3. Edit Movie")
        print("4. Delete Movie")
        print("5. Exit")

    def get_user_choice(self):
        return int(self.get_user_input("Enter your choice: "))

    def get_user_input(self, prompt):
        return input(prompt) 