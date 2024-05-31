Feature: View Product Details

  Scenario: View Product Details
    Given I open the Demoblaze home page
    When I click on a product card
    Then I should be directed to the product details page


  Scenario: Verify Product Price
    Given I open the Demoblaze home page
    When I view the price of a product
    Then I should see the correct price displayed

  Scenario: Verify Product Description
    Given I open the Demoblaze home page
    When I view the description of a product
    Then I should see the correct description displayed


  Scenario: Navigate to Different Product Categories
    Given I open the Demoblaze home page
    When I click on different product categories (e.g., smartphones, laptops)
    Then I should be directed to the corresponding category page


  Scenario: Sort Products by Price
    Given I open the Demoblaze home page
    When I sort products by price (ascending/descending)
    Then Products should be displayed in the correct price order
    
  Scenario: Search for a Product
    Given I open the Demoblaze home page
    When I search for a product
    Then I should see the search results