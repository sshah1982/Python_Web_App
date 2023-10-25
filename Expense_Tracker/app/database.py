import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dotenv_values(".env")

SQLALCHEMY_DATABASE_URL = config['SQLALCHEMY_DATABASE_URL']

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
