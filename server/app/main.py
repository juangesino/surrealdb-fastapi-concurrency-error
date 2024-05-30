from fastapi import FastAPI, Request
from contextlib import asynccontextmanager
from surrealdb import Surreal

from users import (
    get_fake_user,
    create_user,
    delete_user,
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with Surreal("ws://surrealdb:8000/rpc") as database:
        await database.signin(
            {
                "user": "root",
                "pass": "changeme",
            }
        )
        await database.use("demo", "demo")
        app.database = database

        yield


app = FastAPI(lifespan=lifespan)


@app.get("/api/test")
async def test_endpoint(
    request: Request,
):
    inserted_ids = []

    for _ in range(10):
        new_user = get_fake_user()
        inserted_user = await create_user(request.app.database, new_user)
        inserted_ids.append(inserted_user["id"])

    for inserted_id in inserted_ids:
        await delete_user(request.app.database, inserted_id)

    return "ok"
