import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values
from contextlib import contextmanager

config = dotenv_values(".env")

SQLALCHEMY_TEST_DATABASE_URL = config['SQLALCHEMY_TEST_DATABASE_URL']

engine_test = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
SessionLocalTest = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)


@contextmanager
def get_test_db_session():
    db_test = SessionLocalTest()
    try:
        yield db_test
    finally:
        db_test.close()

