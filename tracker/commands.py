from tracker import storage

def add_task(description):
    tasks = storage.load_tasks()
    tasks.append({"description":description,"completed":False})
    storage.save_tasks(tasks)

def list_tasks():
    return storage.load_tasks()

def complete_task(task_id):
    tasks = storage.load_tasks()
    if 0 < task_id <= len(tasks):
        tasks[task_id - 1]["completed"] = True
        storage.save_tasks(tasks)
        return True
    return False

def delete_task(task_id):
    tasks = storage.load_tasks()
    if 0 < task_id <= len(tasks):
        tasks.pop(task_id - 1)
        storage.save_tasks(tasks)
        return True
    return False


