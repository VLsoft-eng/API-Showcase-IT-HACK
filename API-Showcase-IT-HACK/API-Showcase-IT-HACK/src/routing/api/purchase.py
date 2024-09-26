from fastapi import APIRouter, Depends

from src.depends import get_purchase_service
from src.schemas.purchase import PurchaseOut, PurchaseCreate, PurchaseOutExtra
from src.services.purchase_service import PurchaseService

router = APIRouter(prefix="/api/purchase", tags=["api"])


@router.get('.get')
async def get_purchase(purchase_id: int,
                          service: PurchaseService = Depends(get_purchase_service)) -> PurchaseOut:
    return service.get_purchase(purchase_id)

@router.get('.getextra')
async def get_extra_info(purchase_id: int,
                         service: PurchaseService = Depends(get_purchase_service)) -> PurchaseOutExtra:
    return service.get_extra_info(purchase_id)


@router.get('.getlist')
async def get_purchases(access_token: str,
                          service: PurchaseService = Depends(get_purchase_service)) -> list[PurchaseOut]:
    return service.get_list_by_user_token(access_token)


@router.post('.create')
async def create_purchase(schema: PurchaseCreate,
                             service: PurchaseService = Depends(get_purchase_service)) -> PurchaseOut:
    return service.create_purchase(schema)