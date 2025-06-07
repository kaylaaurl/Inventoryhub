from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

Base = declarative_base()

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    message = Column(String(255), nullable=False)
    status = Column(Enum('sent', 'pending', 'read'), default='pending')

url = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"
engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)
