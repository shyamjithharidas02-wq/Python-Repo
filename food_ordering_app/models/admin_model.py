from models.user_model import User


class Admin(User):
    def manage_users(self):
        print(f"⚒️ Admin managing users")
