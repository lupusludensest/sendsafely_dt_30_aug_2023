# Created by rapid at 8/30/2023
Feature: # sendsafely_pytested_bttns_clckd_2

  Scenario: # Clicking buttons. All elements are present and as expected
    Given Loginpage
    Then Click button "Accept" cookies
    Then 1 Click "Features" button. Verify "https://www.sendsafely.com/features/" is open
    Then 2 Hover over "Solutions" button. Verify 5 submenu items with texts are here
    Then 3 Click "Pricing" button. Verify "https://www.sendsafely.com/pricing/" is open
    Then 4 Click "How it Works" button. Verify "https://www.sendsafely.com/howitworks/" is open
    Then 5 Click "Blog" button. Verify "https://blog.sendsafely.com/" is open
    Then 6 Click "Log In" button. Verify "https://www.sendsafely.com/auth/" is open
    And 7 Click "Request Demo" button. Verify "https://www.sendsafely.com/" is open