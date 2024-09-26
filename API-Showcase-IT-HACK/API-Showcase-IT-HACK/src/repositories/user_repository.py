from passlib.context import CryptContext
from sqlalchemy.orm import Session

from ..models.user import User as DBUser
from ..schemas.user import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserRepository:
    def create_user(self, db: Session, user: UserCreate) -> DBUser:
        hashed_password = pwd_context.hash(user.password)
        db_user = DBUser(email=user.email, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user(self, db: Session, id_: int):
        return db.query(DBUser).filter(DBUser.id == id_).first()


    def get_user_by_email(self, db: Session, email: str):
        return db.query(DBUser).filter(DBUser.email == email).first()

