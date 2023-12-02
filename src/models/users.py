from sqlalchemy import Column, String
from .base import Base, BaseMixin

class User(Base, BaseMixin):
    __tablename__ = 'users'
    username = Column(String(255), unique=True)
    name = Column(String(255))
    password = Column(String(255))
