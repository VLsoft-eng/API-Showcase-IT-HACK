from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

    class Config:
        orm_mode = True


class TokenPayloadSchema(BaseModel):
    user_id: str
    expires: Optional[datetime]

    class Config:
        orm_mode = True


class RefreshTokenRequest(BaseModel):
    refresh_token: str

class AccessTokenResponse(BaseModel):
    access_token: str