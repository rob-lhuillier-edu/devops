from fastapi import FastAPI, HTTPException, status
from typing import List
from uuid import UUID
from models import Task, TaskCreate, TaskUpdate
from services import TaskService

app = FastAPI(title="Todo List API - Fil Rouge")

@app.get("/tasks", response_model=List[Task])
async def get_tasks():
    """Retrieve all tasks."""
    return TaskService.get_all_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: UUID):
    """Retrieve a specific task by ID."""
    task = TaskService.get_task_by_id(task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return task

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED)
async def create_task(task_create: TaskCreate):
    """Create a new task."""
    return TaskService.create_task(task_create)

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: UUID, task_update: TaskUpdate):
    """Update an existing task."""
    updated_task = TaskService.update_task(task_id, task_update)
    if not updated_task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return updated_task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: UUID):
    """Delete a task."""
    success = TaskService.delete_task(task_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} not found"
        )
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
