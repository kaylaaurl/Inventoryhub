from sqlalchemy import Column, Integer, String
from config import Base, SessionLocal
from sqlalchemy import Enum

class Notification(Base):
    __tablename__ = 'notifications'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    message = Column(String(255), nullable=False)
    status = Column(Enum('sent', 'pending', 'read'), default='pending')


