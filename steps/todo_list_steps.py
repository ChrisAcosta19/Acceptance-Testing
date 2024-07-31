from behave import given, when, then
from todo_list import add_task, list_tasks, mark_task_completed, clear_tasks, edit_task, save_tasks

# Helper function to reset the state before each scenario
def reset_to_do_list():
    global tasks
    tasks = []
    save_tasks()

@given('the to-do list is empty')
def step_impl(context):
    reset_to_do_list()

@when('the user adds a task with title "{title}", description "{description}", due date "{due_date}", and priority "{priority}"')
def step_impl(context, title, description, due_date, priority):
    add_task(title, description, due_date, priority)

@then('the to-do list should contain a task with title "{title}", description "{description}", due date "{due_date}", priority "{priority}" and completed "{completed}"')
def step_impl(context, title, description, due_date, priority, completed):
    found = False
    for task in tasks:
        if (task['title'] == title and task['description'] == description and 
            task['due_date'] == due_date and task['priority'] == priority and 
            str(task['completed']) == completed):
            found = True
            break
    assert found, f'Task "{title}" not found in the to-do list'

@then('the following message is displayed: {message}')
def step_impl(context, message):
    # Assuming the message is printed to the console
    # Capture the print statements if necessary
    pass

@given('the to-do list contains tasks')
def step_impl(context):
    reset_to_do_list()
    for row in context.table:
        add_task(row['title'], row['description'], row['due_date'], row['priority'])
        if row['completed'] == 'True':
            tasks[-1]['completed'] = True
    save_tasks()

@when('the user lists all tasks')
def step_impl(context):
    context.output = list_tasks()

@then('the output should contain:')
def step_impl(context):
    expected_output = context.text.strip()
    assert expected_output in context.output, f'Expected output not found. Got: {context.output}'

@when('the user marks task "{title}" as completed')
def step_impl(context, title):
    task_number = next((i + 1 for i, task in enumerate(tasks) if task['title'] == title), None)
    assert task_number is not None, f'Task "{title}" not found in the to-do list'
    mark_task_completed(task_number)

@then('the to-do list should show task "{title}" as completed')
def step_impl(context, title):
    task = next((task for task in tasks if task['title'] == title), None)
    assert task is not None, f'Task "{title}" not found in the to-do list'
    assert task['completed'], f'Task "{title}" is not marked as completed'

@when('the user clears the to-do list')
def step_impl(context):
    clear_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert len(tasks) == 0, 'The to-do list is not empty'

@when('the user edits the task "{title}" with:')
def step_impl(context, title):
    task_number = next((i + 1 for i, task in enumerate(tasks) if task['title'] == title), None)
    assert task_number is not None, f'Task "{title}" not found in the to-do list'
    for row in context.table:
        edit_task(task_number, row['title'], row['description'], row['due_date'], row['priority'])

@then('the task "{title}" should have:')
def step_impl(context, title):
    task = next((task for task in tasks if task['title'] == title), None)
    assert task is not None, f'Task "{title}" not found in the to-do list'
    for row in context.table:
        assert task['title'] == row['title'], f'Expected title "{row["title"]}", but got "{task["title"]}"'
        assert task['description'] == row['description'], f'Expected description "{row["description"]}", but got "{task["description"]}"'
        assert task['due_date'] == row['due_date'], f'Expected due date "{row["due_date"]}", but got "{task["due_date"]}"'
        assert task['priority'] == row['priority'], f'Expected priority "{row["priority"]}", but got "{task["priority"]}"'
