from fastapi import FastAPI

from routers.incomes import router as incomes_router


app = FastAPI()

app.include_router(
    incomes_router,
    prefix="/incomes"
)


@app.get("/")
async def index():
    return {"hello": "world"}