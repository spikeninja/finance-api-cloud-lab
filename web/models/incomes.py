import asyncpg
import config

from uuid import uuid4
from datetime import datetime

from schemas.incomes import IncomeRequest, IncomeResponse, IncomeArray


class Incomes:
    def __init__(self):
        pass

    async def _create_connection(self):
        conn = await asyncpg.connect(
            host=config.PG_HOST,
            user=config.PG_USER,
            password=config.PG_PASS,
            database=config.DATABASE
        )

        return conn

    async def create_income(self, income: IncomeRequest) -> dict:
        conn = await self._create_connection()
        query = "INSERT INTO incomes VALUES($1, $2, $3, $4) RETURNING id"
        uuid_ = str(uuid4())
        now_ = datetime.now()
        id_ = await conn.fetchval(
            query,
            uuid_,
            income.user_id,
            income.amount,
            now_
        )
        return {"id": id_}

    async def get_income(self, id_: str):
        conn = await self._create_connection()
        query = "SELECT * FROM incomes WHERE id=$1"
        row = await conn.fetchrow(
            query,
            id_
        )
        print("ROW:", row)
        income = IncomeResponse(
            id=row[0],
            user_id=row[1],
            amount=row[2],
            created_date=row[3]
        )
        return income

    async def get_all_incomes(self, user_id: str) -> IncomeArray:
        conn = await self._create_connection()
        query = "SELECT * FROM incomes WHERE user_id=$1"
        rows = await conn.fetch(
            query,
            user_id
        )
        incomes = []
        for row in rows:
            incomes.append(IncomeResponse(
                id=row[0],
                user_id=row[1],
                amount=row[2],
                created_date=row[3]
            ))
        return IncomeArray(incomes=incomes)

    async def update_income(self, id: str, income: IncomeRequest):
        conn = await self._create_connection()
        query = "UPDATE incomes SET amount=$1 WHERE id=$2 RETURNING id"
        id_ = await conn.fetchval(
            query,
            income.amount,
            id
        )
        return {"id": id_}

    async def delete_income(self, id: str):
        conn = await self._create_connection()
        query = "DELETE FROM incomes WHERE id=$1 RETURNING id"
        id_ = await conn.fetchval(
            query,
            id
        )
        return {"id": id_}
