Feature: User Login

  Scenario: Successful Login
    Given I open the Demoblaze home page
    When I navigate to the login page
    And I enter the registered "152528855" and "152528855"
    And I click the Log in modal button
    Then I should be successfully logged in

  Scenario: Login with Invalid Credentials
    Given I open the Demoblaze home page
    When I navigate to the login page
    And I enter "existing_user" into the username field
    And I enter "invalid_password" into the password field
    And I click the Log in modal button
    Then I should see an alert message indicating invalid credentials

  Scenario: Login with Empty Username
    Given I open the Demoblaze home page
    When I navigate to the login page
    And I leave the username field empty
    And I enter "valid_password" into the password field
    And I click the Log in modal button
    Then The Log in modal should remain visible

  Scenario: Login with Empty Password
    Given I open the Demoblaze home page
    When I navigate to the login page
    And I enter "existing_user" into the username field
    And I leave the password field empty
    And I click the Log in modal button
    Then The Log in modal should remain visible
