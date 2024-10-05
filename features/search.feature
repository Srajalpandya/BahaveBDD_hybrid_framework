Feature:  Search functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to Home page
    When I enter valid product into the Search box field
    And I click on Search button
    Then Valid product should get displayed in Search results

  @search
  Scenario: Search for an invalid product
    Given I got navigated to Home page
    When I enter invalid product into the Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results

  @search
  Scenario: Search without entering any product
    Given I got navigated to Home page
    When I dont enter anything into the search box field
    And I click on search button
    Then Proper message should be displayed in search results

