from enum import Enum
from uuid import UUID
from pydantic import BaseModel, Field
from typing import Optional

class Status(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

class Task(BaseModel):
    id: UUID
    name: str
    status: Status

class TaskCreate(BaseModel):
    name: str
    status: Status = Field(default=Status.TODO)

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    status: Optional[Status] = None
