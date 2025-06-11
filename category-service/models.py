from sqlalchemy import Column, Integer, String
from config import Base, SessionLocal


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255))

