from pydantic import BaseModel, validator, root_validator


class ExpenseBase(BaseModel):
    exp_type: str
    exp_desc: str = None
    amount: float

    class Config:
        fields = {'exp_type': 'exp_type', 'exp_desc': 'exp_desc', 'amount': 'amount'}

    @root_validator(pre=True)
    def check_for_not_null(cls, values):
        if "exp_type" not in values:
            raise ValueError('exp_type was not provided to the model')
        if "amount" not in values:
            raise ValueError('amount was not provided to the model')
        return values

    @validator("exp_type")
    def validate_exp_type(cls, value):
        if len(value) < 1 or len(value) > 100:
            raise ValueError("Expense Type length must be less than or equal to 100")
        return value

    @validator("amount")
    def validate_amount(cls, value):
        if value < 0.0 or value > 10000.0:
            raise ValueError("Amount must be between 1 and 10000")
        return value


class ExpenseCreate(ExpenseBase):
    user_id: int

    class Config:
        fields = {'user_id': 'user_id'}


class ExpenseOut(BaseModel):
    exp_type: str
    exp_desc: str | None = None
    amount: float
    created_date: str
