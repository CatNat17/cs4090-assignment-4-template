from behave import given, when, then
from src.tasks import load_tasks, save_tasks
from datetime import datetime
import pytest

# Step Definitions for Adding a Task

@given('I am on the to-do list page')
def step_given_on_to_do_list_page(context):
    # Simulate being on the to-do list page (could be enhanced for integration tests)
    context.tasks = load_tasks()  # Make sure we are starting with the current tasks list

@when('I add a task with the title "{title}", description "{description}", priority "{priority}", category "{category}", and due date "{due_date}"')
def step_when_add_task(context, title, description, priority, category, due_date):
    # Simulate adding a task
    new_task = {
        "id": len(context.tasks) + 1,
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    context.tasks.append(new_task)
    save_tasks(context.tasks)

@then('the task with the title "{title}" should be added to the task list')
def step_then_task_added(context, title):
    # Check if the task was added to the list
    tasks = load_tasks()
    task_titles = [task['title'] for task in tasks]
    assert title in task_titles, f"Task with title '{title}' was not added."

@when('I try to add a task with the title "{title}", description "{description}", priority "{priority}", category "{category}", and due date "{due_date}"')
def step_when_try_add_task(context, title, description, priority, category, due_date):
    # Try to add task with invalid input
    try:
        new_task = {
            "id": len(context.tasks) + 1,
            "title": title,
            "description": description,
            "priority": priority,
            "category": category,
            "due_date": due_date,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        context.tasks.append(new_task)
        save_tasks(context.tasks)
        context.error = None  # No error if the task is added
    except ValueError as e:
        context.error = str(e)

@then('I should see an error message "{message}"')
def step_then_error_message(context, message):
    # Check if the error message is as expected
    assert context.error == message, f"Expected error message '{message}', but got '{context.error}'"

