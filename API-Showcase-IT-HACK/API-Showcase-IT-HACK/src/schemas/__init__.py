from typing import Optional

from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass


class AllOptional(ModelMetaclass):
    pass

class DeleteSchema(BaseModel):
    id: int
    access_token: str
