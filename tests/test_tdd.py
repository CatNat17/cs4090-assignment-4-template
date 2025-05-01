import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import pytest
from tasks import get_overdue_tasks
from datetime import datetime, timedelta

def test_get_overdue_tasks():
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    future = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    tasks = [
        {"due_date": yesterday, "completed": False},
        {"due_date": future, "completed": False},
        {"due_date": yesterday, "completed": True}
    ]

    overdue = get_overdue_tasks(tasks)
    assert len(overdue) == 1
    assert overdue[0]["due_date"] == yesterday
