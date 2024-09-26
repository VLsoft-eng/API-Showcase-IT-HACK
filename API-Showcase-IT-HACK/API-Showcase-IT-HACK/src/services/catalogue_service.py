from src.models.database import get_db
from src.models.user import Catalogue
from src.repositories.catalogue_repository import CatalogueRepository
from src.schemas import DeleteSchema
from src.schemas.catalogue import CatalogueCreate
from src.utilities.jwt_utils import decode_jwt


class CatalogueService:
    def __init__(self, repository: CatalogueRepository):
        self.repository = repository

    def create_catalogue(self, catalogue_data: CatalogueCreate, distributor) -> Catalogue:

        if distributor:
            db_catalogue = Catalogue(**catalogue_data.model_dump())
            return self.repository.create(next(get_db()), db_catalogue)

        return Catalogue(id=0)

    def get_catalogue(self, id: int) -> Catalogue:
        return self.repository.get(next(get_db()), id)

    def get_catalogues(self, skip: int = 0, limit: int = 10) -> list[Catalogue]:
        return self.repository.get_all(next(get_db()), skip, limit)

    def get_products_list(self, catalogue_id: int):
        return self.repository.get_products_list(next(get_db()), catalogue_id)

    def delete(self, schema: DeleteSchema) -> bool:
        return self.repository.delete(next(get_db()), schema.id)