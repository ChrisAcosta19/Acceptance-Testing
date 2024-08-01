import json
import os

# Define the file path for storing tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description, due_date, priority):
    tasks = load_tasks()
    task = {
        'title': title,
        'description': description,
        'due_date': due_date,
        'priority': priority,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "Completed" if task['completed'] else "Incomplete"
        print(f"{idx}. [{status}] {task['title']} - {task['description']} (Due: {task['due_date']}, Priority: {task['priority']})")

def mark_task_completed(task_number):
    tasks = load_tasks()
    tasks[task_number - 1]['completed'] = True
    save_tasks(tasks)

def clear_tasks():
    tasks = []
    save_tasks(tasks)

def edit_task(task_number, title, description, due_date, priority):
    tasks = load_tasks()
    tasks[task_number - 1]['title'] = title
    tasks[task_number - 1]['description'] = description
    tasks[task_number - 1]['due_date'] = due_date
    tasks[task_number - 1]['priority'] = priority
    save_tasks(tasks)

def main():
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Edit a task")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date (YYYY-MM-DD): ")
            priority = input("Enter task priority (High, Medium, Low): ")
            add_task(title, description, due_date, priority)
            print(f'Task "{title}" added.')
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to mark as completed: "))
            if 0 < task_number <= len(load_tasks()):
                mark_task_completed(task_number)
                print(f'Task {task_number} marked as completed.')
            else:
                print("Invalid task number.")
        elif choice == '4':
            clear_tasks()
            print("All tasks cleared.")
        elif choice == '5':
            task_number = int(input("Enter task number to edit: "))
            if 0 < task_number <= len(load_tasks()):
                title = input("Enter new task title: ")
                description = input("Enter new task description: ")
                due_date = input("Enter new task due date (YYYY-MM-DD): ")
                priority = input("Enter new task priority (High, Medium, Low): ")
                edit_task(task_number, title, description, due_date, priority)
                print(f'Task {task_number} updated.')
            else:
                print("Invalid task number.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
