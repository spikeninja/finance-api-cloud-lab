from datetime import datetime
from pydantic import BaseModel
from typing import List


class IncomeRequest(BaseModel):
    user_id: str
    amount: float


class IncomeResponse(BaseModel):
    id: str
    user_id: str
    amount: float
    created_date: datetime


class IncomeArray(BaseModel):
    incomes: List[IncomeResponse]
