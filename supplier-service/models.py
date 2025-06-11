from sqlalchemy import Column, Integer, String
from config import Base, SessionLocal

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_person = Column(String(100), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    address = Column(String(200))


