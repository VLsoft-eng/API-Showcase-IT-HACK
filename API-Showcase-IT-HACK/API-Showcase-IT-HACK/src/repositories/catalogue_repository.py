from sqlalchemy.orm import Session

from src.models.user import Catalogue, APIProduct


class CatalogueRepository:
    def create(self, db: Session, catalogue: Catalogue) -> Catalogue:
        db.add(catalogue)
        db.commit()
        db.refresh(catalogue)
        return catalogue

    def get(self, db: Session, catalogueid: int) -> Catalogue:
        return db.query(Catalogue).filter(Catalogue.id == catalogueid).first()

    def get_all(self, db: Session, skip: int = 0, limit: int = 10) -> list[Catalogue]:
        return db.query(Catalogue).offset(skip).limit(limit).all()

    def get_products_list(self, db: Session, catalogue_id: int) -> list[APIProduct]:
        return db.query(APIProduct).filter(APIProduct.fk_catalogue == catalogue_id,
                                           APIProduct.is_private != True).all()

    def delete(self, db: Session, id: int):
        try:
            obj = self.get(db, id)
            db.delete(obj)
            db.commit()
            return True
        except:
            return False