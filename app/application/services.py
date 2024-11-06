from app.ports.user_port import UserPort

class UserService:
    def __init__(self, user_port: UserPort):
        self.user_port = user_port

    def get_user(self, user_id: int):
        return self.user_port.get_user_by_id(user_id)
    
    def create_user(self, username: str, email: str):
        return self.user_port.create_user(username, email)
    
    