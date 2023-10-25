from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.sql import expression
from sqlalchemy.orm import relationship, Mapped
from app.models.expenses import *
from typing import List
from sqlalchemy import DateTime
from datetime import timezone


class User(Base):
    __tablename__ = 'user_master'

    user_id = Column('user_id', Integer, primary_key=True, autoincrement=True)
    email = Column('email', String(300), nullable=False, unique=True)
    user_pwd = Column('user_pwd', String(100), nullable=False)
    first_name = Column('first_name', String(100), nullable=False)
    last_name = Column('last_name', String(100), nullable=False)
    role = Column('role', String(10), nullable=False, default='USER')
    birth_date = Column('birth_date', String(15))
    created_date = Column('created_date', DateTime(timezone.utc), nullable=False,  server_default=func.now())
    is_authorized = Column('is_authorized', Boolean, nullable=False, server_default=expression.true())
    expenses: Mapped[List[Expense]] = relationship("Expense", backref="User", passive_deletes=True, lazy="joined")

    def __init__(self, email, user_pwd, first_name, last_name, birth_date):
        self.email = email
        self.user_pwd = user_pwd
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    class Config:
        orm_mode = True

