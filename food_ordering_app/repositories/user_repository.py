class UserRepository:
    def __init__(self):
        self.users_database = {}

    def save_user(self, user):
        self.users_database[user.email] = user

    def find_by_email(self, email):
        return self.users_database.get(email)

    def find_all(self):
        return self.users_database.values()
