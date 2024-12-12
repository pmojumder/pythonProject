Feature: Verify valid invalid cpmbination
  Scenario Outline:feature:verify username and password with valid and invalid combination
    Given open orange HRM browser
    When enter username <username> and <password>
    Then click login button
    Examples:
       |username|password|
       |admin   |admin123|
       |plabani |alex123 |