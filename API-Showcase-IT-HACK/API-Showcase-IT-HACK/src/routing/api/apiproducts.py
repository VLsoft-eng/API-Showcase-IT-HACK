from json import dumps, loads

from fastapi import APIRouter, Depends

from src.depends import get_api_prod_service, get_purchase_service
from src.schemas import DeleteSchema
from src.schemas.api_method import APIMethodInfo
from src.schemas.api_product import APIProductCreate, APIProductOut
from src.schemas.request import RequestMethodSchema, ResponseSchema
from src.services.api_product_service import APIProductService
from src.services.purchase_service import PurchaseService

router = APIRouter(prefix="/api/product", tags=["api"])


@router.get('.get')
async def get_product(id: int,
                          service: APIProductService = Depends(get_api_prod_service)) -> APIProductOut:
    return service.get_api_product(id)

'''
@router.get('.getlist')
async def get_all_products(service: APIProductService = Depends(get_api_prod_service)) -> list [APIProductOut]:
    return service.get_api_products()'''

@router.get('.getmethods')
async def get_product_methods(product_id: int,
                              service: APIProductService = Depends(get_api_prod_service)) -> list[APIMethodInfo]:
    return  service.get_api_product_methods(product_id)

@router.post('.create')
async def create_product(schema: APIProductCreate,
                             service: APIProductService = Depends(get_api_prod_service)) -> APIProductOut:
    return service.create_api_product(schema)

@router.post('.send')
async def send_method(schema: RequestMethodSchema,
                      service: APIProductService = Depends(get_api_prod_service),
                      purchase_service: PurchaseService = Depends(get_purchase_service)):
    json, code, rmain = service.send_request(
        schema.token,
        schema.product_id,
        schema.name,
        loads(schema.body),
        schema.method,
        purchase_service
    )

    return json


@router.post('.delete')
async def delete_product(schema: DeleteSchema,
                             service: APIProductService = Depends(get_api_prod_service)):
    return {
        'success': service.delete(schema)
    }