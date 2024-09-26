from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.apimethod import APIMethod
from src.models.database import get_db
from src.models.user import Catalogue, Distributor, APIProduct
from src.repositories.api_method_repository import APIMethodRepository
from src.schemas import DeleteSchema
from src.schemas.api_method import *
from src.utilities.jwt_utils import decode_jwt


class APIMethodService:
    def __init__(self, repository):
        self.repository = repository

    def create_apimethod(self, schema: APIMethodCreate) -> APIMethodOut:
        decoded_access_token = decode_jwt(schema.access_token)
        if decoded_access_token:
            user_id = decoded_access_token["user_id"]

            db = next(get_db())
            prod: APIProduct = db.query(APIProduct).filter(APIProduct.id == schema.fk_product).first()
            catalogue: Catalogue = db.query(Catalogue).filter(Catalogue.id == prod.fk_catalogue).first()
            distrib: Distributor = db.query(Distributor).filter(Distributor.id==catalogue.fk_distributor).first()

            if user_id != distrib.owner_id:
                raise HTTPException(status_code=401, detail="Err")

            db_method = APIMethod(**schema.dict(exclude=['access_token']))
            return self.repository.create(next(get_db()), db_method)
        raise HTTPException(status_code=404, detail="Err")

    def get_all_apimethods(self) -> list[APIMethodOut]:
        return self.repository.get_all(next(get_db()))

    def get_apimethod_by_name(self, name: str) -> APIMethodOut:
        return self.repository.find_by_name(next(get_db()), name)

    def get(self, method_id):
        return self.repository.get(next(get_db()), method_id)

    def delete(self, schema: DeleteSchema) -> bool:
        return self.repository.delete(next(get_db()), schema.id)