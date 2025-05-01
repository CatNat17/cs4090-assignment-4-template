import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from tasks import filter_tasks_by_completion, search_tasks

@pytest.fixture
def sample_tasks():
    return [
        {"title": "Buy groceries", "description": "Milk and eggs", "completed": False},
        {"title": "Finish project", "description": "Due Monday", "completed": True},
        {"title": "Call Alice", "description": "Birthday", "completed": False}
    ]

@pytest.mark.parametrize("completed,expected_count", [
    (True, 1),
    (False, 2)
])
def test_filter_tasks_by_completion(sample_tasks, completed, expected_count):
    result = filter_tasks_by_completion(sample_tasks, completed)
    assert len(result) == expected_count

@pytest.mark.parametrize("query,expected_count", [
    ("buy", 1),
    ("project", 1),
    ("Alice", 1),
    ("xyz", 0)
])
def test_search_tasks(sample_tasks, query, expected_count):
    result = search_tasks(sample_tasks, query)
    assert len(result) == expected_count
