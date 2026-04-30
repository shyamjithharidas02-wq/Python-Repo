class UserRepository:
    def __init__(self):
        self._users_db = {}

    def save(self, user):
        self._users_db[user.username] = user

    def find_by_username(self, username):
        return self._users_db.get(username)

    def find_all(self):
        return list(self._users_db.values())
