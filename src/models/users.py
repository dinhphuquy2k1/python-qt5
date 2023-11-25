from sqlalchemy import Column, String
from .base import Base, BaseMixin

class User(Base, BaseMixin):
    __tablename__ = 'users'
    name = Column(String(255))