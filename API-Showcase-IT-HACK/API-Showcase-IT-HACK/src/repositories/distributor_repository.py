from sqlalchemy.orm import Session

from src.models.user import Distributor, APIProduct, Catalogue
from src.schemas.user import DistributorCreate, DistributorUpdate, DistributorSchema


class DistributorRepository:
    def create_distributor(self, db: Session, user_id, title):
        db_dist = Distributor(title=title, owner_id=user_id)
        db.add(db_dist)
        db.commit()
        db.refresh(db_dist)
        return db_dist

    def get_distributor(self, db: Session, id: int):
        return db.query(Distributor).filter(Distributor.id == id).first()

    def get_distributor_by_user_id(self, db: Session, uid: int):
        return db.query(Distributor).filter(Distributor.owner_id == uid).first()

    def get_catalogues(self, db: Session, id: int) -> list[Catalogue]:
        return db.query(Catalogue).filter(Catalogue.fk_distributor == id).all()

    def get_all(self, db: Session, skip: int, limit: int):
        return db.query(Distributor).offset(skip).limit(limit).all()

    def update(self, db: Session, schema: DistributorUpdate) -> DistributorSchema:
        obj = db.query(Distributor).filter(Distributor.id == schema.id)
        obj.update(schema.model_dump(exclude=['id', 'access_token']))
        db.commit()
        return obj.first()

    def delete(self, db: Session, id: int):
        try:
            obj = self.get_distributor(db, id)
            db.delete(obj)
            db.commit()
            return True
        except:
            return False
