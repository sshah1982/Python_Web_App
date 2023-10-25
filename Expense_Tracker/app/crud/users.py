from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select, update, delete
from pymysql import IntegrityError
from app.models.users import *
from app.schemas.users import UserBase, UserCreate
from sqlalchemy.sql import text
from app.utils import *


class UserRepository:
    @staticmethod
    def fetch_all(db: Session, skip: int, limit: int, where_clause: str):
        try:
            if where_clause is not None and where_clause != '':
                statement = select(User).limit(limit).offset(skip).where(text(where_clause))
            else:
                statement = select(User).limit(limit).offset(skip)

            recs = db.scalars(statement).unique().fetchall()
            return convert_to_pydantic(recs)

        except Exception as e:
            raise e

    @staticmethod
    def fetch_one(db: Session, uid: int):
        rec = db.get(User, uid)
        rec_list = [rec]

        return convert_to_pydantic(rec_list)

    @staticmethod
    def create(db: Session, user: UserCreate):
        try:
            valid_result = UserCreate(**user.dict())
            db_user = User(valid_result.email, valid_result.user_pwd, valid_result.first_name,
                            valid_result.last_name,
                            valid_result.birth_date if valid_result.birth_date is not None else None)

            db.add(db_user)
            db.commit()
        except ValueError as e:
            raise e
        except IntegrityError as ie:
            raise ie

    @staticmethod
    def update(db: Session, user: UserBase, uid: int):
        try:
            valid_result = UserBase(**user.dict())
            stmt = update(User).where(User.user_id == uid).values(user_pwd=valid_result.user_pwd,
                                                                    first_name=valid_result.first_name,
                                                                    last_name=valid_result.last_name,
                                                                    birth_date=valid_result.birth_date
                                                                    if valid_result.birth_date is not None else None)
            cnt = db.execute(stmt)
            if cnt.rowcount > 0:
                db.commit()
            else:
                raise Exception("This entry does not exist")
        except ValueError as e:
            raise e

    @staticmethod
    def delete(db: Session, uid: int):
        stmt = delete(User).where(User.user_id == uid)
        cnt = db.execute(stmt)
        if cnt.rowcount > 0:
            db.commit()
        else:
            raise Exception("This entry does not exist")
