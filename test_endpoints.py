import requests
import uuid

BASE_URL = "http://127.0.0.1:8000"

def test_workflow():
    print("--- Testing FastAPI Todo List API ---")

    # 1. Create a task
    print("\n1. POST /tasks")
    task_data = {"name": "Test Task", "status": "TODO"}
    response = requests.post(f"{BASE_URL}/tasks", json=task_data)
    assert response.status_code == 201
    task = response.json()
    task_id = task['id']
    print(f"   Created Task: {task}")

    # 2. Get all tasks
    print("\n2. GET /tasks")
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    tasks = response.json()
    assert any(t['id'] == task_id for t in tasks)
    print(f"   All Tasks: {tasks}")

    # 3. Get task by ID
    print(f"\n3. GET /tasks/{task_id}")
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()['id'] == task_id
    print(f"   Task Found: {response.json()}")

    # 4. Update a task
    print(f"\n4. PUT /tasks/{task_id}")
    update_data = {"status": "IN_PROGRESS"}
    response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task['status'] == "IN_PROGRESS"
    print(f"   Updated Task: {updated_task}")

    # 5. Delete a task
    print(f"\n5. DELETE /tasks/{task_id}")
    response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
    assert response.status_code == 204
    print("   Deleted successfully.")

    # 6. Verify deletion
    print("\n6. GET /tasks (Verification)")
    response = requests.get(f"{BASE_URL}/tasks")
    tasks = response.json()
    assert not any(t['id'] == task_id for t in tasks)
    print("   Task is no longer in the list.")

    print("\n--- All tests passed! ---")

if __name__ == "__main__":
    try:
        test_workflow()
    except Exception as e:
        print(f"\nTest failed: {e}")
        if 'response' in locals():
            print(f"Response: {response.status_code} - {response.text}")
