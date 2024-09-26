from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.routing.api.users import router as user_router
from src.routing.api.distributors import router as distributor_router
from src.routing.api.catalogues import router as catalogue_router
from src.routing.api.apiproducts import router as product_router
from src.routing.api.apimethods import router as method_router
from src.routing.api.purchase import router as purchase_router
from src.models.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

##dfd

app.include_router(user_router)
app.include_router(distributor_router)
app.include_router(distributor_router)
app.include_router(catalogue_router)
app.include_router(product_router)
app.include_router(method_router)
app.include_router(purchase_router)