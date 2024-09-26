from sqlalchemy.orm import Session
from sqlalchemy import update
from src.models.token import Token
from src.schemas.token import TokenSchema

class TokenRepository:
    def create_token(self, db: Session, token: TokenSchema, user_id: int):
        db_token = Token(
            user_id=user_id,
            access=token.access_token,
            refresh=token.refresh_token
        )
        db.add(db_token)
        db.commit()
        db.refresh(db_token)
        return db_token

    def delete_token(self, db: Session, refresh_token: str):
        db.query(Token).filter(Token.refresh == refresh_token).delete(synchronize_session=False)
        db.commit()

    def get_token_by_refresh(self, db: Session, refresh_token: str) -> Token:
        return db.query(Token).filter(Token.refresh == refresh_token).first()

    def update_access_token(self, db: Session, token: Token, new_access_token: str):
        db.query(Token).filter(Token.id == token.id).update({Token.access: new_access_token})
        db.commit()
