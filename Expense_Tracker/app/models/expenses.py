from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.sql import func
from app.models import Base
from enum import Enum
from sqlalchemy import DateTime
from datetime import timezone


class ExpenseType(Enum):
    OVERALL = 1
    SHOPPING = 2
    TRAVEL = 3
    GROCERIES = 4
    HOUSE = 5


class Expense(Base):
    __tablename__ = 'expense_master'

    exp_id = Column(Integer, primary_key=True, autoincrement=True)
    exp_type = Column('exp_type', String(100), nullable=False)
    exp_desc = Column('exp_desc', String(500))
    amount = Column('amount', Float,  nullable=False)
    created_date = Column('created_date', DateTime(timezone.utc), nullable=False, server_default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('user_master.user_id', ondelete='CASCADE'), nullable=False)

    def __init__(self, exp_type, exp_desc, amount, user_id):
        self.exp_type = exp_type
        self.exp_desc = exp_desc
        self.amount = amount
        self.user_id = user_id

    class Config:
        orm_mode = True
