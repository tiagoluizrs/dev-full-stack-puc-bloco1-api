import jwt
import datetime
from flask import request, jsonify
from functools import wraps

SECRET_KEY = "nfaK6*H*xub7JpFfsVxQwMZ#&ffDtu9eHdu2anrxQ8*yabJwyTrorY4$Wjhub9zf"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')  # O token geralmente vem no cabeçalho Authorization
        if not token:
            return jsonify({"message": "Token é obrigatório"}), 401

        try:
            jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token inválido"}), 401

        return f(*args, **kwargs)

    return decorated

def generate_token(user_id):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expira em 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
