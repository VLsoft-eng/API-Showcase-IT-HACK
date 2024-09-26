from pydantic import BaseModel

from src.schemas import AllOptional


class PurchaseBase(BaseModel):
    fk_user: int
    fk_product: int

class PurchaseCreate(BaseModel):
    user_token: str
    target_product: int

class PurchaseOut(PurchaseBase):
    id: int
    token: str
    uses: int

    class Config:
        orm_mode = True

class PurchaseOutExtra(BaseModel):
    uses_remain: int
    can_be_used: bool

class PurchaseUpdate(PurchaseBase, metaclass=AllOptional):
    id: int
    access_token: str

    class Config:
        orm_mode = True
