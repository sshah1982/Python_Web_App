from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from dotenv import dotenv_values
from fastapi import status
from base64 import b64encode


security = HTTPBasic()


async def login(credentials: HTTPBasicCredentials = Depends(security)):
    config = dotenv_values(".env")
    if credentials.username == config['APP_LOGIN'] and credentials.password == config['APP_PWD']:
        return credentials
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"}
        )


def basic_auth(username, password):
    token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
    return f'Basic {token}'