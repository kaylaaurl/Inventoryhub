from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    category = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    location = Column(String(100))
    status = Column(Enum('available', 'damaged', 'out_of_stock'), default='available')

url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
