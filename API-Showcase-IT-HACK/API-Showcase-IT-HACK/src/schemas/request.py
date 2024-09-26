from pydantic import BaseModel, Json


class RequestMethodSchema(BaseModel):
    token: str
    product_id: int
    name: str
    body: str
    method: str = 'get'


class ResponseSchema(BaseModel):
    code: int
    body: str
    uses_remain: int