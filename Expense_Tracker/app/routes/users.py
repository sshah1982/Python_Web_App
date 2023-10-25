from fastapi import APIRouter, Depends, Path, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.database import get_db_session
from app.crud.users import *
from app.schemas.users import UserBase, UserCreate
from app.utils import *
from app.auth import *

users = APIRouter(dependencies=[Depends(login)])


@users.get("/user/{uid}")
async def get_one(uid: int = Path(), db=Depends(get_db_session)):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": jsonable_encoder(UserRepository.fetch_one(db, uid))})


@users.get("/users")
async def get_all(request: Request, skip: int, limit: int, db=Depends(get_db_session)):
    params = str(request.query_params)
    recs = UserRepository.fetch_all(db, skip, limit,
                                    extract_search_clause_for_users(params))
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": jsonable_encoder(recs)})


@users.post("/user")
async def create(user: UserCreate, db=Depends(get_db_session)):
    UserRepository.create(db, user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Successfully Created"})


@users.put("/user/{uid}")
async def update(user: UserBase, uid: int = Path(), db=Depends(get_db_session)):
    UserRepository.update(db, user, uid)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Successfully Updated"})


@users.delete("/user/{uid}")
async def delete(uid: int = Path(), db=Depends(get_db_session)):
    UserRepository.delete(db, uid)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Successfully Deleted"})


