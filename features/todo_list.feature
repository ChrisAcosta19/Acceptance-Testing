# language: en

Feature: To-Do List Manager

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task with title "Buy groceries", description "Buy fruits and vegetables", due date "2024-07-30", and priority "High"
    Then the to-do list should contain a task with title "Buy groceries", description "Buy fruits and vegetables", due date "2024-07-30", priority "High" and completed "False"
    And the following message is displayed: Task "Buy groceries" added.

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | title         | description                 | due_date   | priority | completed |
      | Buy groceries | Buy fruits and vegetables   | 2024-07-30 | High     | True      |
      | Pay bills     | Pay electricity and water   | 2024-07-31 | Medium   | False     |
    When the user lists all tasks
    Then the output should contain:
      """
      1. [Completed] Buy groceries - Buy fruits and vegetables (Due: 2024-07-30, Priority: High)
      2. [Incomplete] BPay bills - Pay electricity and water (Due: 2024-07-31, Priority: Medium)
      """

  Scenario: Mark a task as completed
    Given the to-do list contains tasks:
      | title         | description               | due_date   | priority | completed   |
      | Buy groceries | Buy fruits and vegetables | 2024-07-30 | High     | False       |
    When the user marks task "Buy groceries" as completed
    Then the to-do list should show task "Buy groceries" as completed
    And the following message is displayed: Task 1 marked as completed.

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | title         | description               | due_date   | priority | completed |
      | Buy groceries | Buy fruits and vegetables | 2024-07-30 | High     | True      |
      | Pay bills     | Pay electricity and water | 2024-07-31 | Medium   | False     |
    When the user clears the to-do list
    Then the to-do list should be empty
    And the following message is displayed: All tasks cleared.

  Scenario: Edit a task in the to-do list
    Given the to-do list contains tasks:
      | title         | description               | due_date   | priority | completed   |
      | Buy groceries | Buy fruits and vegetables | 2024-07-30 | High     | False       |
    When the user edits the task "Buy groceries" with:
      | title         | description        | due_date   | priority |
      | Buy groceries | Buy fresh produce  | 2024-08-01 | Medium   |
    Then the task "Buy groceries" should have:
      | title         | description        | due_date   | priority |
      | Buy groceries | Buy fresh produce  | 2024-08-01 | Medium   |
