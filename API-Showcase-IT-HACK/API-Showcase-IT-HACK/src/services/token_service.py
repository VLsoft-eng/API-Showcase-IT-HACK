from httpx import delete
from sqlalchemy.orm import Session
from src.repositories.token_repository import TokenRepository
from src.utilities.jwt_utils import decode_jwt, generate_access_token, sign_jwt
from src.schemas.token import TokenSchema
from src.models.database import get_db

class TokenService:
    def __init__(self, repository: TokenRepository):
        self.repository = TokenRepository()

    def create_token(self, token: TokenSchema, user_id: int):
        return self.repository.create_token(next(get_db()), token, user_id)

    def delete_token(self, refresh_token: str):
        self.repository.delete_token(next(get_db()), refresh_token)

    def refresh_access_token(self, refresh_token: str) -> str:
        token = self.repository.get_token_by_refresh(next(get_db()), refresh_token)

        if token is None:
            return ("token is none", 1)

        decoded_refresh_token = decode_jwt(refresh_token, is_refresh_token=True)

        if decoded_refresh_token:
            user_id = decoded_refresh_token["user_id"]
            new_access_token = generate_access_token(user_id)

            self.repository.update_access_token(next(get_db()), token, new_access_token)

            return (new_access_token, 0)
        else:
            return self.delete_token(refresh_token)
