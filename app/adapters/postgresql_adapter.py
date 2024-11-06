from app.ports.user_port import UserPort
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class PostgresqlAdapter(UserPort):
    def __init__(self) -> None:
        pass

    def get_user_by_id(self, user_id: int):
        return User.query.get(user_id)
    
    def create_user(self, username: str, email: str):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    