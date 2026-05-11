from services.decorators import logger
from models.user_model import User


class AuthService:
    def __init__(self, repo):
        self.repo = repo
        self.current_user = None

    @logger
    def register(self):
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        if not User.validate_email(email):
            print("❌ Invalid email")
            return

        user = User(name, email, password)
        self.repo.save_user(user)
        print("✅ Registration successful")

    @logger
    def login(self):
        email = input("Enter name: ")
        password = input("Enter password: ")

        user = self.repo.find_by_email(email)

        if not user:
            print("❌ User not found")
            return

        if user.verify_password(password):
            self.current_user = user
            print(f"✅ Welcome {user.name}")
        else:
            print("❌ Incorrect password")

    @logger
    def logout(self):
        if self.current_user:
            print(f"🔒 {self.current_user.name} logged out")
            self.current_user = None
        else:
            print("❌ No user logged in")
