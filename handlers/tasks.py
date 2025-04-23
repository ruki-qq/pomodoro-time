from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("")
async def get_tasks():
    return []


@router.post("/{task_id}")
async def create_task():
    return {"created_task": "ok"}
