import json
import os



FILE_PATH = "tasks.json"

def load_tasks():
    print("DEBUG: Loading tasks...")
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=4)