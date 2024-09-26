from src.models.database import get_db
from src.models.user import Catalogue
from src.repositories.distributor_repository import DistributorRepository
from src.schemas import DeleteSchema
from src.schemas.user import DistributorSchema, DistributorCreate, DistributorUpdate, DistributorDelete
from src.utilities.jwt_utils import decode_jwt


class DistributorService:
    def __init__(self, repository: DistributorRepository):
        self.repository = repository

    def get_distributor_for_user(self, user_id) -> DistributorSchema:
        return self.repository.get_distributor_by_user_id(next(get_db()), user_id)

    def create_distributor_for_user(self, schema: DistributorCreate) -> DistributorSchema:
        decoded_access_token = decode_jwt(schema.access_token)
        if decoded_access_token:
            user_id = decoded_access_token["user_id"]

            return self.repository.create_distributor(next(get_db()), user_id, schema.title)
        return DistributorSchema(id=-1)


    def get_catalogues(self, distributor_id: int) -> list[Catalogue]:
        return self.repository.get_catalogues(next(get_db()), distributor_id)

    def get_all(self, skip: int, limit: int) -> list[DistributorSchema]:
        return self.repository.get_all(next(get_db()), skip, limit)

    def update(self, schema: DistributorUpdate) -> DistributorSchema:
        return self.repository.update(next(get_db()), schema)

    def delete(self, schema: DeleteSchema) -> bool:
        return self.repository.delete(next(get_db()), schema.id)