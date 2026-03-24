import json
import os
from pathlib import Path
from typing import List
from models import Task

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "tasks.json"

def ensure_storage_exists():
    """Create data directory and tasks.json if they don't exist."""
    if not DATA_DIR.exists():
        DATA_DIR.mkdir()
    if not DATA_FILE.exists():
        with open(DATA_FILE, "w") as f:
            json.dump([], f)

def load_tasks() -> List[Task]:
    """Load tasks from the JSON file."""
    ensure_storage_exists()
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Task(**task) for task in data]
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks: List[Task]):
    """Save tasks to the JSON file."""
    ensure_storage_exists()
    with open(DATA_FILE, "w") as f:
        # Convert UUID to string for JSON serialization
        tasks_data = [task.model_dump() for task in tasks]
        # JSON serializer needs help with UUIDs usually, 
        # but model_dump() with pydantic v2 might handle it or we convert manually
        for task in tasks_data:
            task['id'] = str(task['id'])
        json.dump(tasks_data, f, indent=4)
