from fastapi import APIRouter

from models.incomes import Incomes
from schemas.incomes import IncomeResponse, IncomeRequest, IncomeArray


router = APIRouter()
incomes_model = Incomes()


@router.get("/", response_model=IncomeArray)
async def get_all_incomes(user_id: str):
    incomes = await incomes_model.get_all_incomes(user_id)
    return incomes


@router.get("/{id}", response_model=IncomeResponse)
async def get_income(id_: str):
    income = await incomes_model.get_income(id_)
    return income


@router.post("/")
async def create_income(income: IncomeRequest):
    id_ = await incomes_model.create_income(income)
    return id_


@router.put("/{id}")
async def update_income(id: str, income: IncomeRequest):
    id_ = await incomes_model.update_income(id, income)
    return id_


@router.delete("/{id}")
async def delete_income(id: str):
    id_ = await incomes_model.delete_income(id)
    return id_
