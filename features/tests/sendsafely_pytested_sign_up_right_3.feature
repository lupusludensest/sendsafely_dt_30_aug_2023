# Created by rapid at 9/1/2023
Feature: # test_sendsafely_pytested_sign_up_right_3

  Scenario: # Sign up by randomized email. Verify "https://www.sendsafely.com/auth/#signup" is open.
    Given Loginpage
    Then Click button "Accept" cookies
    Then 1 Click button "Sign up Now"
    Then 2 Enter the email randomized to "Email address" empty field
    Then 3 Click on "Get Started" button
    And 4 Verify "https://www.sendsafely.com/auth/#signup" is open
