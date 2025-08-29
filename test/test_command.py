import os
import json
import pytest
from tracker import commands, storage

TEST_FILE = "test_tasks.json"

# Override the storage file path for testing
storage.FILE_PATH = TEST_FILE

@pytest.fixture(autouse=True)
def clean_file():
    # Setup: clear test file
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)
    yield
    # Teardown: remove test file after test
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_add_task():
    commands.add_task("Test Task")
    tasks = storage.load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["description"] == "Test Task"
    assert tasks[0]["completed"] is False

def test_complete_task():
    commands.add_task("Complete me")
    result = commands.complete_task(1)
    tasks = storage.load_tasks()
    assert result is True
    assert tasks[0]["completed"] is True

def test_delete_task():
    commands.add_task("Delete me")
    result = commands.delete_task(1)
    tasks = storage.load_tasks()
    assert result is True
    assert len(tasks) == 0

def test_invalid_task_id():
    commands.add_task("Keep me")
    result = commands.complete_task(99)
    assert result is False
