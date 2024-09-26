from typing import Dict, Any

from fastapi import APIRouter, Depends

from src.depends import get_catalogue_service, get_distributor_service
from src.models.user import Catalogue, APIProduct
from src.schemas import DeleteSchema
from src.schemas.api_product import APIProductOut
from src.schemas.catalogue import CatalogueOut, CatalogueCreate, CatalogueCreateRequest
from src.services.catalogue_service import CatalogueService
from src.services.distributor_service import DistributorService
from src.utilities.jwt_utils import decode_jwt

router = APIRouter(prefix="/api/catalogue", tags=["api"])


@router.get('.get')
async def get_catalogue(catalogue_id: int,
                        service: CatalogueService = Depends(get_catalogue_service)) -> CatalogueOut:
    return service.get_catalogue(catalogue_id)


@router.post('.create', response_model=CatalogueOut)
async def create_catalogue(schema: CatalogueCreateRequest,
                           service: CatalogueService = Depends(get_catalogue_service),
                           dservice: DistributorService = Depends(get_distributor_service)):
    decoded_token = decode_jwt(schema.access_token)
    uid = int(decoded_token['user_id'])
    distributor = dservice.get_distributor_for_user(uid)

    return service.create_catalogue(CatalogueCreate(
            fk_distributor=distributor.id,
            title=schema.title,
            description=schema.description), distributor)

@router.get('.getproducts')
async def get_products(catalogue_id: int,
                       service: CatalogueService = Depends(get_catalogue_service)) -> list[APIProductOut]:
    return service.get_products_list(catalogue_id)

@router.post('.delete')
async def delete_catalogue(schema: DeleteSchema,
                            service: CatalogueService = Depends(get_catalogue_service)):
    return {
        'success': service.delete(schema)
    }