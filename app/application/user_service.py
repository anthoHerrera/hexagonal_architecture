# pylint: disable=missing-class-docstring
from app.adapters.database import User, db

class UserService:
    @staticmethod
    def create_user(name: str, email: str):
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_user(user_id: int) -> User:
        return User.query.get(user_id)
    
    @staticmethod
    def get_all_users() -> list:
        return User.query.all()
    