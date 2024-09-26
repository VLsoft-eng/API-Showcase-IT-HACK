
from sqlalchemy import Column, Integer, String, ForeignKey

from src.models.database import Base


class APIMethod(Base):
    __tablename__ = "apimethods"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String)

    fk_product = Column(Integer, ForeignKey('apiproduct.id'))

