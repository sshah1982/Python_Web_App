from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError


app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                        content=jsonable_encoder({"detail": "Incorrect username or password"}))


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}))


@app.exception_handler(ValueError)
async def value_error_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}))


@app.exception_handler(IntegrityError)
async def db_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content={"error": "Duplicate Email Entry"})


@app.exception_handler(Exception)
async def generic_exception_handler(request, exc):
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        content=jsonable_encoder({"error": str(exc)}))

