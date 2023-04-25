from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Todo(BaseModel):
    id: str
    task: str
    done: bool
    deleted: bool

todos = [
    Todo(id="1",task="Create am App", done=False, deleted=False),
    Todo(id="2",task="Deploy the App", done=False, deleted=False),
    Todo(id="3",task="Deploy the App 2", done=False, deleted=False),
]

@app.get("/todos", response_model=list[Todo])
def get_todos():
    return todos
