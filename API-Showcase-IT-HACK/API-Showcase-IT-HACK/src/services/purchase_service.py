import random

from src.models.database import get_db
from src.models.user import Purchase
from src.repositories.purchase_repository import PurchaseRepository
from src.schemas.purchase import PurchaseCreate, PurchaseOut, PurchaseOutExtra
from src.utilities.jwt_utils import decode_jwt


class PurchaseService:
    def __init__(self, repository: PurchaseRepository):
        self.repository = repository

    def generate_token(self) -> str:
        return str(random.getrandbits(128))

    def create_purchase(self, schema: PurchaseCreate) -> PurchaseOut:
        decoded_access_token = decode_jwt(schema.user_token)
        if decoded_access_token:
            user_id = decoded_access_token["user_id"]
            product_id = schema.target_product

            ####
            # validate payment
            ####

            p_token = self.generate_token()

            db_purchase = Purchase(fk_user=user_id,
                                   fk_product=product_id,
                                   token=p_token)
            return self.repository.create(next(get_db()), db_purchase)
        return PurchaseOut(id=-1)

    def get_purchase(self, id: int) -> PurchaseOut:
        return self.repository.get(next(get_db()), id)

    def get_by_user_and_product(self, user_id: int, product_id: int) -> Purchase:
        return self.repository.get_by_user_and_product(user_id, product_id)

    def get_by_token(self, token: str):
        return self.repository.get_by_token(next(get_db()), token)

    def increase_uses(self, purchase_id: int) -> None:
        self.repository.increase_uses(next(get_db()), purchase_id)

    def can_be_used(self, purchase_id: int) -> bool:
        return self.repository.can_be_used(next(get_db()), purchase_id)

    def uses_remain(self, purchase_id) -> int:
        self.repository.uses_remain(next(get_db()), purchase_id)

    def get_list_by_user_token(self, access_token) -> list[PurchaseOut]:
        decoded_access_token = decode_jwt(access_token)
        if decoded_access_token:
            user_id = decoded_access_token["user_id"]

            return self.repository.get_all_for_user(next(get_db()), user_id)
        return []

    def get_extra_info(self, purchase_id: int):
        ur = self.uses_remain(purchase_id)
        cu = self.can_be_used(purchase_id)
        return PurchaseOutExtra(
            uses_remain=ur if ur else -1,
            can_be_used=cu if cu else False
        )
