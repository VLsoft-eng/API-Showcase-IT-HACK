from sqlalchemy.orm import Session

from src.models.apimethod import APIMethod
from src.models.user import APIProduct
from src.schemas.api_method import APIMethodInfo


class APIProductRepository:
    def create(self, db: Session, product: APIProduct) -> APIProduct:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def get(self, db: Session, pid: int) -> APIProduct:
        return db.query(APIProduct).filter(APIProduct.id == pid).first()

    def get_all_products(self, db: Session, pid: int) -> list[APIMethodInfo]:
        return db.query(APIMethod).filter(APIMethod.fk_product == pid).all()

    def get_all(self, db: Session, skip: int = 0, limit: int = 10) -> list[APIProduct]:
        return db.query(APIProduct).filter(APIProduct.is_private != True).offset(skip).limit(limit).all()

    def delete(self, db: Session, id: int):
        try:
            obj = self.get(db, id)
            db.delete(obj)
            db.commit()
            return True
        except:
            return False