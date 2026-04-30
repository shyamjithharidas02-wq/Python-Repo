from repositories.user_repository import UserRepository
from services.auth_service import AuthServiceImpl


def main():
    repo = UserRepository()
    auth_service = AuthServiceImpl(repo)

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Admin Panel")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            auth_service.register_user()
        elif choice == "2":
            auth_service.login_user()
        elif choice == "3":
            auth_service.show_all_users()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
