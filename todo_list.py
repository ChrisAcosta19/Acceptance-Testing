import json
import os

# Define the file path for storing tasks
TASKS_FILE = 'tasks.json'

# Load tasks from the file if it exists
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'r') as file:
        tasks = json.load(file)
else:
    tasks = []

def save_tasks():
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description, due_date, priority):
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    save_tasks()
    print(f'Task "{title}" added.')

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Incomplete"
        print(f"{idx}. [{status}] {task['title']} - {task['description']} (Due: {task['due_date']}, Priority: {task['priority']})")

def mark_task_completed(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        save_tasks()
        print(f'Task {task_number} marked as completed.')
    else:
        print("Invalid task number.")

def clear_tasks():
    global tasks
    tasks = []
    save_tasks()
    print("All tasks cleared.")

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (High, Medium, Low): ")
            add_task(title, description, due_date, priority)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: "))
            mark_task_completed(task_number)
        elif choice == '4':
            clear_tasks()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
