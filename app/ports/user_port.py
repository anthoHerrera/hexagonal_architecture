from abc import ABC, abstractmethod

class UserPort(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id: int):
        pass

    @abstractmethod
    def create_user(self, username: str, email: str):
        pass
    