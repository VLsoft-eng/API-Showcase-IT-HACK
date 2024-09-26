from sqlalchemy import Column, Integer, ForeignKey, String

from src.models.database import Base


class Token(Base):
    __tablename__ = "token"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    access = Column(String)
    refresh = Column(String)
