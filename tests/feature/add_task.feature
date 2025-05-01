Feature: Add a task to the to-do list

  Scenario: User adds a new task with valid input
    Given I am on the to-do list page
    When I add a task with the title "Buy groceries", description "Milk, eggs, bread", priority "High", category "Personal", and due date "2025-05-01"
    Then the task with the title "Buy groceries" should be added to the task list

  Scenario: User tries to add a task without a title
    Given I am on the to-do list page
    When I try to add a task with the title "", description "No title", priority "Low", category "Work", and due date "2025-06-01"
    Then I should see an error message "Task title is required"

  Scenario: User adds a task with invalid date format
    Given I am on the to-do list page
    When I try to add a task with the title "Invalid date task", description "Test invalid date", priority "Medium", category "Other", and due date "invalid-date"
    Then I should see an error message "Invalid date format"

