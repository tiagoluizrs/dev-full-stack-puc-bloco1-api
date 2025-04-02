from extensions import db
from utils.password import check_password, hash_password
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
                email=data["email"],
                password=hash_password(data["password"])
            )
            db.session.add(user)
            db.session.commit()

            return user