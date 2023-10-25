import requests
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth

config = dotenv_values(".env")

auth_header = HTTPBasicAuth(config['APP_LOGIN'], config['APP_PWD'])


def test_create_expense_failure_bad_request_400():
    exp_json = {
        "exp_type": "OVERALL",
        "amount": 4000
    }

    res = requests.post(url='http://127.0.0.0:8000/expense', json=exp_json, auth=auth_header)
    assert res.status_code == 400


def test_get_all_expenses_success():
    res = requests.get(url='http://127.0.0.0:8000/expenses?limit=10&skip=0', auth=auth_header)
    assert(res.status_code == 200)


def test_get_one_expense_success():
    res = requests.get(url='http://127.0.0.0:8000/expense/1', auth=auth_header)
    assert(res.status_code == 200)


def test_update_expense_success():
    exp_json = {
        "exp_type": "HOUSE",
        "amount": 4000,
        "user_id": 1
    }
    res = requests.put(url='http://127.0.0.0:8000/expense/2', json=exp_json, auth=auth_header)
    assert(res.status_code == 200)


def delete_expense_success():
    res = requests.delete(url='http://127.0.0.0:8000/expense/7', auth=auth_header)
    assert(res.status_code == 200)
