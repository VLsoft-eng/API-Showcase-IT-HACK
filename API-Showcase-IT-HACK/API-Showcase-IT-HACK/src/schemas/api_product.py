from pydantic import BaseModel

from src.schemas import AllOptional


class APIProductBase(BaseModel):
    title: str
    description: str
    max_uses: int = -1

class APIProductCreate(APIProductBase):
    fk_catalogue: int
    access_token: str

class APIProductUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    max_uses: int | None = None
    id: int
    access_token: str

class APIProductOut(APIProductBase):
    id: int

    class Config:
        orm_mode = True
