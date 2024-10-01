Feature: Register Account Functionality


  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter mandatory fields
    And I click on Countinue button
    Then Account should get created

  Scenario: Regiser with all fields
    Given I navigate to Register Page
    When I enter all fields
    And I click on Countinue button
    Then Account should get created

  Scenario: Register with a duplicate email address
    Given I navigate to Register Page
    When I enter details into all fields except email field
    And I enter existing accounts email into email field
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed

  Scenario: Register with empty fields
    Given I navigate to Register Page
    When I dont enter anything into the fields
    And I click on Continue button
    Then Proper warning messages for every mandatory fields should be displayed
