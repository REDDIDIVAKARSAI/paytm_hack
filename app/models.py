from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    items = Column(String)
    total = Column(Integer)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    source = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)
    bill_id = Column(Integer)
    payment_id = Column(Integer)
    score = Column(Integer)