from datetime import datetime, timedelta

import jwt

from src.schemas.token import TokenSchema

EXPIRATION_TIME = timedelta(minutes=30)
REFRESH_TOKEN_EXPIRATION_TIME = timedelta(days=7)
SECRET_KEY = 'super_secret_key'
ALGORITHM = "HS256"


def sign_jwt(user_id: str):
    access_token_payload = {
        "user_id": user_id,
        "expires": str(datetime.utcnow() + EXPIRATION_TIME)
    }
    refresh_token_payload = {
        "user_id": user_id,
        "expires": str(datetime.utcnow() + REFRESH_TOKEN_EXPIRATION_TIME)
    }

    access_token = jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)
    refresh_token = jwt.encode(refresh_token_payload, SECRET_KEY, algorithm=ALGORITHM)

    return TokenSchema(access_token=access_token, refresh_token=refresh_token)


def decode_jwt(token: str, is_refresh_token: bool = False) -> dict:
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    if datetime.strptime(decoded_token["expires"], "%Y-%m-%d %H:%M:%S.%f") >= datetime.utcnow():
        return decoded_token
    else:
        return None


def generate_access_token(user_id: str) -> str:
    access_token_payload = {
        "user_id": user_id,
        "expires": str(datetime.utcnow() + EXPIRATION_TIME)
    }
    return jwt.encode(access_token_payload, SECRET_KEY, algorithm=ALGORITHM)