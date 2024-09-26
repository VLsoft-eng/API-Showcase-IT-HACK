# repositories/apimethod_repository.py
from sqlalchemy.orm import Session

from src.models.apimethod import APIMethod


class APIMethodRepository:
    def create(self, db: Session, apimethod: APIMethod) -> APIMethod:
        db.add(apimethod)
        db.commit()
        db.refresh(apimethod)
        return apimethod

    def get_all(self, db: Session) -> list[APIMethod]:
        return db.query(APIMethod).all()

    def get(self, db: Session, id: int) -> list[APIMethod]:
        return db.query(APIMethod).filter(APIMethod.id == id).first()

    def find_by_name(self, db: Session, name: str) -> APIMethod:
        return db.query(APIMethod).filter(APIMethod.name == name).first()

    def delete(self, db: Session, id: int):
        try:
            obj = self.get(db, id)
            db.delete(obj)
            db.commit()
            return True
        except:
            return False
