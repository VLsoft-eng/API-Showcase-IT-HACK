from typing import List

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, Mapped

from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_superuser = Column(Boolean, default=False)

    distributor = relationship("Distributor", uselist=False, backref="owner")


class Distributor(Base):
    __tablename__ = "distributor"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))

    catalogues: Mapped[List["Catalogue"]] = relationship()


class Catalogue(Base):
    __tablename__ = "catalogue"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    fk_distributor = Column(Integer, ForeignKey('distributor.id'))


class APIProduct(Base):
    __tablename__ = "apiproduct"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    is_private = Column(Boolean, default=False)

    max_uses = Column(Integer, default=-1)

    fk_catalogue = Column(Integer, ForeignKey('catalogue.id'))


# TODO: Rename to 'access'
class Purchase(Base):
    __tablename__ = "purchase"

    id = Column(Integer, primary_key=True)
    fk_user = Column(Integer, ForeignKey('user.id'))
    fk_product = Column(Integer, ForeignKey('apiproduct.id'))

    token = Column(String)

    uses = Column(Integer, default=0)


