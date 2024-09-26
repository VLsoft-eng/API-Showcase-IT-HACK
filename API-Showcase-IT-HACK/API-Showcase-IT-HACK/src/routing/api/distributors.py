from fastapi import APIRouter, Depends

from src.depends import get_distributor_service
from src.schemas import DeleteSchema
from src.schemas.catalogue import CatalogueOut
from src.schemas.user import DistributorSchema, DistributorCreate, DistributorUpdate, DistributorDelete
from src.services.distributor_service import DistributorService

router = APIRouter(prefix="/api/distributor", tags=["api"])


@router.get('.get')
async def get_distributor(user_id: int,
                          service: DistributorService = Depends(get_distributor_service)) -> DistributorSchema:
    return service.get_distributor_for_user(user_id)

@router.get('.getlist')
async def get_all_distributors(skip: int, limit: int,
                          service: DistributorService = Depends(get_distributor_service)) -> list[DistributorSchema]:
    return service.get_all(skip, limit)

@router.get('.getcatalogues')
async def get_all_catalogues_for_distributor(distributor_id: int,
                                             service: DistributorService =
                                             Depends(get_distributor_service)) -> list[CatalogueOut]:
    return service.get_catalogues(distributor_id)

@router.post('.create')
async def create_distributor(schema: DistributorCreate,
                             service: DistributorService = Depends(get_distributor_service)) -> DistributorSchema:
    return service.create_distributor_for_user(schema)

@router.post('.update')
async def update_distributor(schema: DistributorUpdate,
                             service: DistributorService = Depends(get_distributor_service)) -> DistributorSchema:
    return service.update(schema)

@router.post('.delete')
async def delete_distributor(schema: DeleteSchema,
                             service: DistributorService = Depends(get_distributor_service)):
    return {
        'success': service.delete(schema)
    }