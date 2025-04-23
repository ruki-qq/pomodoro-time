from pydantic import BaseModel


class TaskBase(BaseModel):
    name: str
    pomodoro_cnt: int
    category_id: int


class Task:
    id: int
