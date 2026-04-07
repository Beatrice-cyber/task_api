from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

app = FastAPI()

class Task(BaseModel):
    content: str

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/tasks")
def create_task(task: Task):
    db = SessionLocal()
    task_id = str(uuid.uuid4())
    db_task = TaskModel(task_id=task_id, content=task.content)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    db.close()

    return {"task_id": db_task.task_id, "content": db_task.content}

@app.get("/tasks")
def get_tasks():
    db = SessionLocal()

    tasks = db.query(TaskModel).all()

    db.close()

    return [{"task_id": t.task_id, "content": t.content} for t in tasks]

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    db = SessionLocal()
    task = db.query(TaskModel).filter(TaskModel.task_id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        db.close()
        return {"message": "deleted"}
    db.close()
    return {"error": "not found"}

class TaskModel(Base):
    __tablename__ = "tasks"

    task_id = Column(String, primary_key=True, index=True)
    content = Column(String)
Base.metadata.create_all(bind=engine)