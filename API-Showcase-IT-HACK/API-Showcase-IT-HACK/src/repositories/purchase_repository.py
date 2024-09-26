from sqlalchemy.orm import Session

from src.models.user import Purchase, APIProduct
from src.schemas.purchase import PurchaseOut


class PurchaseRepository:
    def create(self, db: Session, purchase: Purchase) -> Purchase:
        db.add(purchase)
        db.commit()
        db.refresh(purchase)
        return purchase

    def get(self, db: Session, pid: int) -> Purchase:
        return db.query(Purchase).filter(Purchase.id == pid).first()

    def delete(self, db: Session, id: int):
        try:
            obj = self.get(db, id)
            db.delete(obj)
            db.commit()
            return True
        except:
            return False

    def get_by_user_and_product(self, db: Session, user_id: int, product_id: int) -> Purchase:
        return db.query(Purchase).filter(Purchase.fk_user == user_id,
                                         Purchase.fk_product == product_id).first()

    def get_all_for_user(self, db: Session, user_id: int) -> list[Purchase]:
        return db.query(Purchase).filter(Purchase.fk_user == user_id).all()

    def can_be_used(self, db: Session, pid: int) -> bool:
        purchase: Purchase = self.get(db, pid)
        product: APIProduct = db.query(APIProduct).filter(APIProduct.id == purchase.fk_product).first()
        return True if (product.max_uses == None or product.max_uses < 0) else product.max_uses > purchase.uses

    def increase_uses(self, db: Session, pid: int) -> None:
        purchase: Purchase = self.get(db, pid)
        purchase.uses += 1
        db.commit()

    def uses_remain(self, db: Session, pid: int) -> int:
        purchase: Purchase = self.get(db, pid)
        product: APIProduct = db.query(APIProduct).filter(APIProduct.id == purchase.fk_product).first()
        return -1 if (product.max_uses == None or purchase.uses == None or product.max_uses == -1) else\
            product.max_uses - purchase.uses

    def get_by_token(self, db: Session, token: str):
        purchase: Purchase = db.query(Purchase).filter(Purchase.token==token).first()
        return purchase