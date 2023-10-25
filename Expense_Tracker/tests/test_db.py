from tests import *
from app.models.users import *
from app.models.expenses import *
from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError


def test_users_get_all_no_records():
    with get_test_db_session() as db_test_u:
        records = db_test_u.scalars(select(User).limit(10).offset(0)).unique().fetchall()
        assert len(records) == 0


def test_user_create():
    try:
        user = User("ooooooo@zemoso.com", "12345", "abc", "pqr", "24/11/1982")
        with get_test_db_session() as db_test_u:
            db_test_u.add(user)
            db_test_u.commit()
    except IntegrityError as ie:
        raise ie


def test_user_get_all_one_record():
    with get_test_db_session() as db_test_u:
        recs = db_test_u.scalars(select(User).limit(10).offset(0)).unique().fetchall()
        assert len(recs) == 1


def test_user_get_one():
    with get_test_db_session() as db_test_u:
        rec = db_test_u.get(User, 1)
        assert rec.user_id == 1


def test_user_delete():
    with get_test_db_session() as db_test_u:
        delete(User).where(User.user_id == 1)
        db_test_u.commit()


def test_exp_get_all_no_records():
    with get_test_db_session() as db_test_e:
        records = db_test_e.scalars(select(Expense).limit(10).offset(0)).unique().fetchall()
        assert len(records) == 0


def test_exp_create():
    exp = Expense("HOUSE", "House Expenses", 4000.0, 1)
    with get_test_db_session() as db_test_e:
        db_test_e.add(exp)
        db_test_e.commit()


def test_exp_get_all_one_record():
    with get_test_db_session() as db_test_e:
        recs = db_test_e.scalars(select(Expense).limit(10).offset(0)).unique().fetchall()
        assert len(recs) == 1


def test_exp_get_one():
    with get_test_db_session() as db_test_e:
        rec = db_test_e.get(Expense, 1)
        assert rec.exp_id == 1


def test_exp_delete():
    with get_test_db_session() as db_test_u:
        delete(Expense).where(Expense.exp_id == 1)
        db_test_u.commit()
