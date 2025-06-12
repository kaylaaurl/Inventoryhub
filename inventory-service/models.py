from sqlalchemy import Column, Integer, String
from config import Base, SessionLocal
from sqlalchemy import Enum


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String(100))
    status = Column(Enum('available', 'damaged', 'out_of_stock'), default='available')


