from behave import given, when, then
from todo_list import clear_tasks, load_tasks, add_task, edit_task, mark_task_completed

@given('the to-do list is cleared')
def step_clear_todo_list(context):
    clear_tasks()

@when('I add a task with title "{title}", description "{description}", due date "{due_date}", and priority "{priority}"')
def step_add_task(context, title, description, due_date, priority):
    add_task(title, description, due_date, priority)

@then('the task list should contain a task with title "{title}" and status "{status}"')
def step_verify_task_added(context, title, status):
    tasks = load_tasks()
    for task in tasks:
        if task['title'] == title:
            assert task['completed'] == (status == "Completed")
            return
    assert False, f'Task with title "{title}" not found'

@given('there is a task with title "{title}", description "{description}", due date "{due_date}", and priority "{priority}"')
def step_given_task_exists(context, title, description, due_date, priority):
    clear_tasks()
    add_task(title, description, due_date, priority)

@when('I list all tasks')
def step_list_tasks(context):
    context.tasks = load_tasks()

@then('I should see the task with title "{title}", description "{description}", due date "{due_date}", and priority "{priority}"')
def step_verify_listed_task(context, title, description, due_date, priority):
    for task in context.tasks:
        if task['title'] == title and task['description'] == description and task['due_date'] == due_date and task['priority'] == priority:
            return
    assert False, f'Task with title "{title}" not found'

@when('I mark the task with title "{title}" as completed')
def step_mark_task_completed(context, title):
    tasks = load_tasks()
    for idx, task in enumerate(tasks):
        if task['title'] == title:
            mark_task_completed(idx + 1)
            return
    assert False, f'Task with title "{title}" not found'

@then('the task with title "{title}" should have status "Completed"')
def step_verify_task_completed(context, title):
    tasks = load_tasks()
    for task in tasks:
        if task['title'] == title:
            assert task['completed'] == True
            return
    assert False, f'Task with title "{title}" not found'

@when('I clear the to-do list')
def step_clear_todo_list(context):
    clear_tasks()

@then('the task list should be empty')
def step_verify_list_empty(context):
    tasks = load_tasks()
    assert not tasks, "Task list is not empty"

@when('I edit the task with title "{old_title}" to have title "{new_title}", description "{new_description}", due date "{new_due_date}", and priority "{new_priority}"')
def step_edit_task(context, old_title, new_title, new_description, new_due_date, new_priority):
    tasks = load_tasks()
    for idx, task in enumerate(tasks):
        if task['title'] == old_title:
            edit_task(idx + 1, new_title, new_description, new_due_date, new_priority)
            return
    assert False, f'Task with title "{old_title}" not found'

@then('the task list should contain a task with title "{title}", description "{description}", due date "{due_date}", priority "{priority}", and status "{status}"')
def step_verify_edited_task(context, title, description, due_date, priority, status):
    tasks = load_tasks()
    for task in tasks:
        if task['title'] == title and task['description'] == description and task['due_date'] == due_date and task['priority'] == priority:
            assert task['completed'] == (status == "Completed")
            return
    assert False, f'Task with title "{title}" not found'
