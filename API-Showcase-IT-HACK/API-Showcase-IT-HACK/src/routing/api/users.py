from fastapi import APIRouter
from fastapi import Depends
from fastapi.openapi.models import Response
from ...depends import get_user_service, get_token_service
from ...repositories.user_repository import pwd_context
from ...schemas.token import TokenSchema, RefreshTokenRequest, AccessTokenResponse
from ...schemas.user import *
from ...services.token_service import TokenService
from ...services.user_service import UserService
from ...utilities.jwt_utils import sign_jwt
from fastapi import Request


router = APIRouter(prefix="/api/user", tags=["api"])


@router.get(".get", response_model=UserOut)
async def get_user(access_token: str, service: UserService = Depends(get_user_service)):
    return service.get_user(access_token)


@router.post(".create")
async def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    return service.create_user(user)
    #return {"message": "User created successfully"}


@router.post(".login", response_model=TokenSchema)
async def login(authData: UserCreate, service: UserService = Depends(get_user_service),
                token_service: TokenService = Depends(get_token_service)):
    user = service.get_user_by_email(authData.email)

    if pwd_context.verify(authData.password, user.hashed_password):
        tokens = sign_jwt(user.id)
        token_service.create_token(tokens, user.id)
        return {
            'access_token': tokens.access_token,
            'refresh_token': tokens.refresh_token
        }

    return {
        'access_token': '',
        'refresh_token': ''
    }


@router.post(".refresh_access_token", response_model=AccessTokenResponse)
async def refresh_access_token(request: RefreshTokenRequest, service: TokenService = Depends(get_token_service)):
    new_access_token, status = service.refresh_access_token(request.refresh_token)

    return {
        'access_token': new_access_token
    }
