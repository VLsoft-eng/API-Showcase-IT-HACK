from pydantic import BaseModel
from typing import Optional

from src.schemas import AllOptional


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    is_superuser: bool = False

    class Config:
        orm_mode = True


class DistributorBase(BaseModel):
    title: str


class DistributorCreate(DistributorBase):
    access_token: str

class DistributorUpdate(BaseModel):
    title: str | None = None
    id: int
    access_token: str

class DistributorDelete(BaseModel):
    id: int
    access_token: str


class DistributorSchema(DistributorBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True