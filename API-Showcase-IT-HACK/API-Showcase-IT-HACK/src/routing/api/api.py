from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["api"])

def get_router():
    return router