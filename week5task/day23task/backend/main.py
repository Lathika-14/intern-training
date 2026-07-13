from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal
from schemas import TaskCreate, TaskResponse
from database import engine, Base
import crud

app = FastAPI()

Base.metadata.create_all(bind=engine)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create Task
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)


# Get All Tasks
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


# Get Single Task
@app.get("/tasks/{id}", response_model=TaskResponse)
def get_task(id: int, db: Session = Depends(get_db)):
    task = crud.get_task(db, id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# Update Task
@app.put("/tasks/{id}", response_model=TaskResponse)
def update_task(id: int, updated_task: TaskCreate, db: Session = Depends(get_db)):
    task = crud.update_task(db, id, updated_task)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# Delete Task
@app.delete("/tasks/{id}")
def delete_task(id: int, db: Session = Depends(get_db)):
    task = crud.delete_task(db, id)

    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}