from pydantic import BaseModel

from src.schemas import AllOptional


class CatalogueBase(BaseModel):
    title: str
    description: str

class CatalogueCreate(CatalogueBase):
    fk_distributor: int

class CatalogueCreateRequest(CatalogueBase):
    access_token: str

class CatalogueUpdate(CatalogueBase):
    id: int
    access_token: str

class CatalogueOut(CatalogueBase):
    id: int

    class Config:
        orm_mode = True
