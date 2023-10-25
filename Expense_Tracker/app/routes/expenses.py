from fastapi import APIRouter, Path, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from app.database import get_db_session
from app.crud.expenses import *
from app.schemas.expenses import ExpenseBase, ExpenseCreate
from app.utils import *
from app.auth import *

expenses = APIRouter(dependencies=[Depends(login)])


@expenses.get("/expense/{eid}")
async def get_one(eid: int = Path(), db=Depends(get_db_session)):
    return JSONResponse(status_code=status.HTTP_200_OK, content={"data": jsonable_encoder(ExpenseRepository.fetch_one(db, eid))})


@expenses.get("/expenses")
async def get_all(request: Request, skip: int, limit: int, db=Depends(get_db_session)):
    params = str(request.query_params)
    return JSONResponse(status_code=status.HTTP_200_OK,
                        content={"data": jsonable_encoder(ExpenseRepository.fetch_all(db, skip, limit,
                                          extract_search_clause_for_expenses(params)))})


@expenses.post("/expense")
async def create(expense: ExpenseCreate, db=Depends(get_db_session)):
    ExpenseRepository.create(db, expense)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Successfully Created"})


@expenses.put("/expense/{eid}")
async def update(expense: ExpenseBase, eid: int = Path(), db=Depends(get_db_session)):
    ExpenseRepository.update(db, expense, eid)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Successfully Updated"})


@expenses.delete("/expense/{eid}")
async def delete(eid: int = Path(), db=Depends(get_db_session)):
    ExpenseRepository.delete(db, eid)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Successfully Deleted"})


