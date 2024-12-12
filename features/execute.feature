Feature: Executing first bdd tetscase
  Scenario:Login username and password validation
    Given open orange HRM browser
    When enter valid credental username "Admin" and password "admin123"
    Then click login button
    And Home page loaded successfully



