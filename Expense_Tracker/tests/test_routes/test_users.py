import requests
from dotenv import dotenv_values
from requests.auth import HTTPBasicAuth

config = dotenv_values(".env")

auth_header = HTTPBasicAuth(config['APP_LOGIN'], config['APP_PWD'])


def test_create_user_failure_bad_request_400():
    user_json = {
        "first_name": "llll",
        "last_name": "mmm",
        "user_pwd": "12345678",
        "birth_date": "24/11/1982"
    }

    res = requests.post(url='http://127.0.0.0:8000/user', json=user_json, auth=auth_header)
    assert res.status_code == 400


def test_get_all_users_success():
    res = requests.get(url='http://127.0.0.0:8000/users?limit=10&skip=0', auth=auth_header)
    assert(res.status_code == 200)
    assert(res.json() is not None)


def test_get_one_user_success():
    res = requests.get(url='http://127.0.0.0:8000/user/1', auth=auth_header)
    assert(res.status_code == 200)


def test_update_user_success():
    user_json = {
        "first_name": "llll",
        "last_name": "mmm",
        "user_pwd": "12345678",
        "birth_date": "24/11/1982"
    }
    res = requests.put(url='http://127.0.0.0:8000/user/1', json=user_json, auth=auth_header)
    assert(res.status_code == 200)


def test_update_user_failure_bad_request_400():
    user_json = {
        "last_name": "mmm",
        "user_pwd": "12345678",
        "birth_date": "24/11/1982"
    }
    res = requests.put(url='http://127.0.0.0:8000/user/1', json=user_json, auth=auth_header)
    assert(res.status_code == 400)


def delete_user_success():
    res = requests.delete(url='http://127.0.0.0:8000/user/7', auth=auth_header)
    assert(res.status_code == 200)