from fastapi import APIRouter, Depends

from src.depends import get_api_method_service
from src.schemas import DeleteSchema
from src.schemas.api_method import APIMethodCreate, APIMethodOut
from src.services.api_method_service import APIMethodService

router = APIRouter(prefix="/api/method", tags=["api"])


@router.get('.get')
async def get_method(method_id: int,
                          service: APIMethodService = Depends(get_api_method_service)) -> APIMethodOut:
    return service.get(method_id)

@router.post('.create')
async def create_method(schema: APIMethodCreate,
                             service: APIMethodService = Depends(get_api_method_service)) -> APIMethodOut:
    return service.create_apimethod(schema)

@router.post('.delete')
async def delete_method(schema: DeleteSchema,
                             service: APIMethodService = Depends(get_api_method_service)):
    return {
        'success': service.delete(schema)
    }