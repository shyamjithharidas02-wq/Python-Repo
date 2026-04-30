from abc import ABC, abstractmethod


class AuthService(ABC):

    @abstractmethod
    def register_user(self):
        pass

    @abstractmethod
    def login_user(self):
        pass
