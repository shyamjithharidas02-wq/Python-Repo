import random
import string

from services.auth_interface import AuthService
from models.user import User


class AuthServiceImpl(AuthService):
    def __init__(self, repo):
        self.repo = repo

    def _generate_username(self, first, last):
        rand = random.randint(1000, 9999)
        return f"{first.lower()}.{last.lower()}{rand}"

    def _generate_password(self, length=8):
        chars = string.ascii_letters + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    # register
    def register_user(self):
        print("\n--- Create Account ---")

        first = input("First Name: ")
        last = input("Last Name: ")
        email = input("Email: ")
        place = input("Place: ")

        username = self._generate_username(first, last)
        password = self._generate_password()

        user = User(first, last, email, place, username, password)
        self.repo.save(user)

        print("\n✅ Account Created Successfully")
        print(f"Username: {username}")
        print(f"Password: {password}")

    # login
    def login_user(self):
        print("\n--- Login ---")

        username = input("Username: ")
        password = input("Password: ")

        user = self.repo.find_by_username(username)

        if not user:
            print("❌ User not found!")
            return

        if user.verify_password(password):
            print(f"✅ Welcome {user.f_name}")
        else:
            print("❌ Invalid password")

        user.record_login()
        self._show_user_dashboard(user)

    def _show_user_dashboard(self, user):
        print("\n" + "─" * 40)
        print(f"  👤  {user.get_full_name()}")
        print(f"  📧  {user.email}")
        print(f"  📍  {user.place}")
        print(f"  🆔  {user.username}")
        print(f"  📅  Joined : {user.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  🔑  Logins : {user.login_count}")
        print(f"  🕐  Last   : {user.last_login.strftime('%Y-%m-%d %H:%M:%S')}")
        print("─" * 40)

    # admin
    def show_all_users(self):
        users = self.repo.find_all()

        print(f"\n── ALL REGISTERED USERS ({len(users)}) ───────────────")

        for user in users:
            print(f"  • {user.username:<25} {user.get_full_name()}")
