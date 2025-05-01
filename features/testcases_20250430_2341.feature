Feature: Search product by name

    Scenario: Search for an existing product by name
        Given I am on the online store page
        When I enter "dress" in the search field
        And I click the search button
        Then I should see the product "dress" in the search results

    Scenario: Search for a non-existent product by name
        Given I am on the online store page
        When I enter "nonexistentproduct" in the search field
        And I click the search button
        Then I should see a message indicating that no results were found for the search
