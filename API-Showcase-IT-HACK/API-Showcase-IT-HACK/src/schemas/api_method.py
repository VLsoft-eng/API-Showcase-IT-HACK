from pydantic import BaseModel

from src.schemas import AllOptional


class APIMethodBase(BaseModel):
    name: str
    address: str

class APIMethodCreate(APIMethodBase):
    fk_product: int
    access_token: str

class APIMethodUpdate(BaseModel):
    name: str | None = None
    address: str | None = None
    id: int
    access_token: str

class APIMethodOut(APIMethodBase):
    id: int

    class Config:
        orm_mode = True

class APIMethodInfo(BaseModel):
    name: str
    id: int
