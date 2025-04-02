from utils.password import check_password
from utils.token import generate_token

class AuthenticationController:
    def login(self, data):
        from models.User import User
        user = User.query.filter_by(email=data["email"]).first()
        if user:
            validate = check_password(data["password"], user.password)
            if validate:
                return {
                    "user": user,
                    "token": generate_token(user.id)
                }
            else:
                return None
        else:
            return None

    def register(self, data):
        from models.User import User
        user = User.query.filter_by(email=data["email"]).first()
        if user:
            return None
        else:
            user = User(
                name=data["name"],
                email=data["email"],
                password=data["password"]
            )
            user.save()
            return user