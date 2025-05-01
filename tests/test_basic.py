import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from tasks import load_tasks, save_tasks, generate_unique_id, filter_tasks_by_priority, filter_tasks_by_category
import os

TEST_FILE = "test_tasks.json"

def setup_function():
    # Reset test file for each test
    with open(TEST_FILE, "w") as f:
        f.write("[]")

def teardown_function():
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)

def test_save_and_load_tasks():
    sample_tasks = [{"id": 1, "title": "Test", "priority": "High", "category": "Work"}]
    save_tasks(sample_tasks, TEST_FILE)
    loaded = load_tasks(TEST_FILE)
    assert loaded == sample_tasks

def test_generate_unique_id_empty():
    assert generate_unique_id([]) == 1

def test_generate_unique_id_nonempty():
    tasks = [{"id": 1}, {"id": 5}]
    assert generate_unique_id(tasks) == 6

def test_filter_tasks_by_priority():
    tasks = [{"priority": "High"}, {"priority": "Low"}]
    result = filter_tasks_by_priority(tasks, "High")
    assert result == [{"priority": "High"}]

def test_filter_tasks_by_category():
    tasks = [{"category": "School"}, {"category": "Work"}]
    result = filter_tasks_by_category(tasks, "Work")
    assert result == [{"category": "Work"}]
