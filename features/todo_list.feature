Feature: To-Do List Management
  As a user
  I want to manage my to-do list
  So that I can keep track of my tasks

  Background:
    Given the to-do list is cleared

  Scenario: Add a task to the to-do list
    When I add a task with title "Buy groceries", description "Buy milk, eggs, and bread", due date "2024-08-01", and priority "High"
    Then the task list should contain a task with title "Buy groceries" and status "Incomplete"

  Scenario: List all tasks in the to-do list
    Given there is a task with title "Buy groceries", description "Buy milk, eggs, and bread", due date "2024-08-01", and priority "High"
    When I list all tasks
    Then I should see the task with title "Buy groceries", description "Buy milk, eggs, and bread", due date "2024-08-01", and priority "High"

  Scenario: Mark a task as completed
    Given there is a task with title "Buy groceries", description "Buy milk, eggs, and bread", due date "2024-08-01", and priority "High"
    When I mark the task with title "Buy groceries" as completed
    Then the task with title "Buy groceries" should have status "Completed"

  Scenario: Clear the entire to-do list
    Given there is a task with title "Buy groceries", description "Buy milk, eggs, and bread", due date "2024-08-01", and priority "High"
    When I clear the to-do list
    Then the task list should be empty

  Scenario: Edit an existing task in the to-do list
    Given there is a task with title "Buy groceries", description "Buy milk, eggs, and bread", due date "2024-08-01", and priority "High"
    When I edit the task with title "Buy groceries" to have title "Buy vegetables", description "Buy carrots and spinach", due date "2024-08-02", and priority "Medium"
    Then the task list should contain a task with title "Buy vegetables", description "Buy carrots and spinach", due date "2024-08-02", priority "Medium", and status "Incomplete"
