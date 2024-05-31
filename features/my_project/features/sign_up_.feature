Feature: User Sign Up

  Scenario: Sign Up with Existing Username
    Given I open the Demoblaze home page
    When I click the Sign up button
    And I enter "152528855" into the username field
    And I enter "152528855" into the password field
    And I click the Sign up modal button
    Then I should see an alert message indicating the username is already taken

  Scenario: Sign Up with Invalid Password
    Given I open the Demoblaze home page
    When I click the Sign up button
    And I enter "new_user" into the username field
    And I enter "invalid" into the password field
    And I click the Sign up modal button
    Then I should see an alert message indicating the password is invalid

  Scenario: Sign Up with Empty Fields
    Given I open the Demoblaze home page
    When I click the Sign up button
    And I leave the username field empty
    And I leave the password field empty
    And I click the Sign up modal button
    Then I should see alert messages indicating both fields are required
