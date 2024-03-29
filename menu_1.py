from auth_3 import UserAuthentication
auth=UserAuthentication()

class MainMenu:
    # def __init__(self, auth_system):
    #     self.auth_system = auth_system
    
    def display_menu(self):
        print("\n=== Main Menu ===")
        print("1. Register")
        print("2. Log In")
        print("3. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                role = input("Enter your role (user/admin): ").lower()
                if role not in ['user', 'admin']:
                    print("Invalid role. Defaulting to 'user'.")
                    role = 'user'
                auth.register(username, password,role)
            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                auth.login(username, password)
                 # Placeholder for logged-in user actions
            elif choice == "3":
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    
                    
                    
    

