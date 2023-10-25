import dotenv
from dotenv import load_dotenv

from app.exceptions.exception_handlers import *

from app.routes.users import *
from app.routes.expenses import *

from app.encryption import *

from app.middleware.rate_limiter import *

from app.models import Base
from app.database import engine
from tests import engine_test

app = FastAPI()

app.include_router(users)
app.include_router(expenses)


app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(ValueError, value_error_exception_handler)
app.add_exception_handler(IntegrityError, db_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


#app.add_middleware(RateLimitingMiddleware)


@app.middleware("http")
async def add_version_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Version"] = "v1.1.0"
    return response


@app.on_event("startup")
def startup_event():
    load_dotenv('.env')

    Base.metadata.create_all(bind=engine)

    #Create Test DB Tables
    Base.metadata.create_all(bind=engine_test)

    dotenv_file = dotenv.find_dotenv()
    dotenv.set_key(dotenv_file, "ENC_KEY", generate_key())


@app.on_event("shutdown")
def shutdown_event():
    Base.metadata.drop_all(bind=engine_test)

