# repositories
from src.repositories.api_method_repository import APIMethodRepository
from src.repositories.api_product_repository import APIProductRepository
from src.repositories.catalogue_repository import CatalogueRepository
from src.repositories.distributor_repository import DistributorRepository
from src.repositories.purchase_repository import PurchaseRepository
from src.repositories.token_repository import TokenRepository
from src.repositories.user_repository import UserRepository
from src.services.api_method_service import APIMethodService
from src.services.api_product_service import APIProductService
from src.services.catalogue_service import CatalogueService
from src.services.purchase_service import PurchaseService
from src.services.token_service import TokenService
from src.services.user_service import UserService
from src.services.distributor_service import DistributorService

user_repository = UserRepository()
token_repository = TokenRepository()
distributor_repository = DistributorRepository()
catalogue_repository = CatalogueRepository()
purchase_repository = PurchaseRepository()
api_prod_repository = APIProductRepository()
api_method_repository = APIMethodRepository()

# services

user_service = UserService(user_repository)
token_service = TokenService(token_repository)
distributor_service = DistributorService(distributor_repository)
catalogue_service = CatalogueService(catalogue_repository)
purchase_service = PurchaseService(purchase_repository)
api_prod_service = APIProductService(api_prod_repository)
api_method_service = APIMethodService(api_method_repository)


######
def get_user_service():
    return user_service


def get_token_service():
    return token_service


def get_distributor_service():
    return distributor_service


def get_catalogue_service():
    return catalogue_service


def get_purchase_service():
    return purchase_service


def get_api_prod_service():
    return api_prod_service


def get_api_method_service():
    return api_method_service
