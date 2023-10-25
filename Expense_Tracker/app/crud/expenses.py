from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from app.models.expenses import *
from app.schemas.expenses import ExpenseBase, ExpenseCreate
from sqlalchemy.sql import text


class ExpenseRepository:
    @staticmethod
    def fetch_all(db: Session, skip: int, limit: int, where_clause: str):
        if where_clause is not None and where_clause != '':
            statement = select(Expense).limit(limit).offset(skip).where(text(where_clause))
        else:
            statement = select(Expense).limit(limit).offset(skip)
        return db.scalars(statement).all()

    @staticmethod
    def fetch_one(db: Session, eid: int):
        return db.get(Expense, eid)

    @staticmethod
    def create(db: Session, expense: ExpenseCreate):
        try:
            valid_result = ExpenseCreate(**expense.dict())
            db_exp = Expense(valid_result.exp_type, valid_result.exp_desc if valid_result.exp_desc is not None
                                else None, valid_result.amount, valid_result.user_id)
            db.add(db_exp)
            db.commit()
        except ValueError as e:
            raise e
        except IntegrityError as ie:
            raise ie

    @staticmethod
    def update(db: Session, expense: ExpenseBase, eid: int):
        try:
            valid_result = ExpenseBase(**expense.dict())
            stmt = update(Expense).where(Expense.exp_id == eid).values(exp_type=valid_result.exp_type,
                                                                      exp_desc=valid_result.exp_desc if valid_result.exp_desc is not None
                                                                      else None, amount=valid_result.amount)
            cnt = db.execute(stmt)
            if cnt.rowcount > 0:
                db.commit()
            else:
                raise Exception("This entry does not exist")
        except ValueError as e:
            raise e

    @staticmethod
    def delete(db: Session, eid: int):
        stmt = delete(Expense).where(Expense.exp_id == eid)
        db.execute(stmt)
        cnt = db.execute(stmt)
        if cnt.rowcount > 0:
            db.commit()
        else:
            raise Exception("This entry does not exist")
