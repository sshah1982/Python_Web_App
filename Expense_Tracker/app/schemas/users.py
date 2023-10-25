from pydantic import BaseModel, validator, root_validator
from typing import Optional, List
import re
from app.schemas.expenses import ExpenseOut


class UserBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: Optional[str] = None
    user_pwd: str

    class Config:
        fields = {'first_name': 'first_name', 'last_name': 'last_name', 'birth_date': 'birth_date', 'user_pwd': 'user_pwd'}

    @root_validator(pre=True)
    def check_for_not_null(cls, values):
        if "first_name" not in values:
            raise ValueError('first_name was not provided to the model')
        if "last_name" not in values:
            raise ValueError('last_name was not provided to the model')
        if "user_pwd" not in values:
            raise ValueError('user_pwd was not provided to the model')
        return values

    @validator("first_name")
    def validate_first_name(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError("First Name length must be less than or equal to 100")
        return value

    @validator("last_name")
    def validate_last_name(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError("Last Name length must be less than or equal to 100")
        return value

    @validator("user_pwd")
    def validate_pwd(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError("Password length must be less than or equal to 100")
        return value


class UserCreate(UserBase):
    email: str

    class Config:
        fields = {'email': 'email'}

    @validator("email")
    def validate_email(cls, value):
        if len(value) < 1 or len(value) > 300:
            raise ValueError("Email length must be less than or equal to 300" )
        if not bool(re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', value)):
            raise ValueError("Email is invalid")
        return value


class UserOut(BaseModel):
    first_name: str
    last_name: str
    birth_date: str | None = None
    email: str
    created_date: str
    expenses: List = [ExpenseOut]
