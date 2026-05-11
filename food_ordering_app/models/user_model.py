class User:
    total_user = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password
        User.total_user += 1

    def verify_password(self, password):
        return self.__password == password

    @staticmethod
    def validate_email(email):
        return "@" in email

    @classmethod
    def get_total_users(cls):
        print(f"👤 Total Users: {cls.total_user}")
