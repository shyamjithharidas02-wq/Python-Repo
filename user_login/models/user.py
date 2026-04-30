from datetime import datetime


class User:
    def __init__(self, f_name, l_name, email, place, username, password):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.place = place
        self.username = username
        self.__password = password

        self.created_at = datetime.now()
        self.login_count = 0
        self.last_login = None

    def verify_password(self, password):
        return self.__password == password

    def record_login(self):
        self.login_count += 1
        self.last_login = datetime.now()

    def get_full_name(self):
        return f"{self.f_name} {self.l_name}"
