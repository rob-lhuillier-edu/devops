from uuid import UUID, uuid4
from typing import List, Optional
from models import Task, TaskCreate, TaskUpdate
import persistence

class TaskService:
    @staticmethod
    def get_all_tasks() -> List[Task]:
        return persistence.load_tasks()

    @staticmethod
    def get_task_by_id(task_id: UUID) -> Optional[Task]:
        tasks = persistence.load_tasks()
        for task in tasks:
            if task.id == task_id:
                return task
        return None

    @staticmethod
    def create_task(task_create: TaskCreate) -> Task:
        tasks = persistence.load_tasks()
        new_task = Task(
            id=uuid4(),
            name=task_create.name,
            status=task_create.status
        )
        tasks.append(new_task)
        persistence.save_tasks(tasks)
        return new_task

    @staticmethod
    def update_task(task_id: UUID, task_update: TaskUpdate) -> Optional[Task]:
        tasks = persistence.load_tasks()
        for i, task in enumerate(tasks):
            if task.id == task_id:
                if task_update.name is not None:
                    tasks[i].name = task_update.name
                if task_update.status is not None:
                    tasks[i].status = task_update.status
                persistence.save_tasks(tasks)
                return tasks[i]
        return None

    @staticmethod
    def delete_task(task_id: UUID) -> bool:
        tasks = persistence.load_tasks()
        initial_len = len(tasks)
        tasks = [t for t in tasks if t.id != task_id]
        if len(tasks) < initial_len:
            persistence.save_tasks(tasks)
            return True
        return False
