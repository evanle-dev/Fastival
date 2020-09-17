from importlib import import_module

from fastapi import Depends
from fastapi import Header, HTTPException

from api import app, settings


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


users_router = import_module('api.routes.v{}_{}.users'.format(settings.major_version, settings.minor_version)).router
items_router = import_module('api.routes.v{}_{}.items'.format(settings.major_version, settings.minor_version)).router

app.include_router(
    router=users_router,
)
app.include_router(
    router=items_router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
