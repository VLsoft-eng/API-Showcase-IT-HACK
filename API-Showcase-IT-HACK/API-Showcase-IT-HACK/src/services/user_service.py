from fastapi import Depends

from src.repositories.user_repository import UserRepository, pwd_context
from src.models.database import get_db
from ..schemas.user import UserCreate, UserOut
from ..utilities.jwt_utils import decode_jwt


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user(self, access_token: str) -> UserOut:
        decoded_access_token = decode_jwt(access_token)
        if decoded_access_token:
            user_id = decoded_access_token["user_id"]

            return self.repository.get_user(next(get_db()), user_id)
        return UserOut(id=-1)

    def get_user_by_email(self, email: str):
        return self.repository.get_user_by_email(next(get_db()), email)

    def create_user(self, user: UserCreate):
        return self.repository.create_user(next(get_db()), user)

    def compare_user(self, authData: UserCreate):
        user = self.repository.get_user_by_email(next(get_db()),authData.email)
        return pwd_context.verify(authData.password, user.hashed_password)
