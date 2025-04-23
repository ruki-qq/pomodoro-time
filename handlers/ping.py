from fastapi import APIRouter

router = APIRouter(prefix="/ping", tags=["ping"])


@router.get("/db")
async def ping_db():
    return {"pong_db": "ok"}


@router.get("/app")
async def ping_app():
    return {"pong_app": "ok"}
