import json

import requests

from src.models.apimethod import APIMethod
from src.models.database import get_db
from src.models.user import APIProduct, Catalogue, Distributor
from src.repositories.api_product_repository import APIProductRepository
from src.schemas import DeleteSchema
from src.schemas.api_product import APIProductCreate, APIProductOut
from src.services.purchase_service import PurchaseService
from src.utilities.jwt_utils import decode_jwt


class APIProductService:
    def __init__(self, repository: APIProductRepository):
        self.repository = repository

    def create_api_product(self, schema: APIProductCreate):
        decoded_access_token = decode_jwt(schema.access_token)
        if decoded_access_token:
            user_id = decoded_access_token["user_id"]

            db = next(get_db())
            catalogue: Catalogue = db.query(Catalogue).filter(Catalogue.id == schema.fk_catalogue).first()
            distrib: Distributor = db.query(Distributor).filter(Distributor.id == catalogue.fk_distributor).first()

            if user_id != distrib.owner_id:
                return APIProductOut(id=-1)

            db_prod = APIProduct(**schema.dict(exclude=['access_token']))
            return self.repository.create(next(get_db()), db_prod)
        return APIProductOut(id=-1)

    def get_api_product(self, id: int):
        return self.repository.get(next(get_db()), id)

    def get_api_products(self):
        return self.repository.get_all(next(get_db()))

    def send_request(self, token: str, product_id: int, method_name: str, json_data: dict, send_method: str,
                     purchase_service: PurchaseService):
        db = next(get_db())
        purchase = purchase_service.get_by_token(token)

        if not purchase:
            return {}, 1, 0

        if not purchase_service.can_be_used(purchase.id):
            return {}, 4, 0

        method: APIMethod = db.query(APIMethod).filter(APIMethod.fk_product == product_id,
                                                       APIMethod.name == method_name).first()

        if not method:
            return {}, 2, 0

        uri = method.address

        purchase_service.increase_uses(purchase.id)
        response = requests.get(uri, params=json_data).json()

        return response, 0, purchase_service.uses_remain(purchase.id)

    def get_api_product_methods(self, product_id: int):
        return self.repository.get_all_products(next(get_db()), product_id)

    def delete(self, schema: DeleteSchema) -> bool:
        return self.repository.delete(next(get_db()), schema.id)
