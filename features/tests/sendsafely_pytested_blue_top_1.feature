# Created by rapid at 8/30/2023
Feature: # sendsafely_pytested_blue_top_1

  Scenario: # Testing the blue top of the app. 12 steps. All elements are present and as expected
    Given Loginpage
    Then Click button "Accept" cookies
    Then 1 Picture SENDSAFELY '/img/ss_logo_60_343.png' is present
    Then 2 Picture Globe as a Schema '/img/globe_lines.png' is present
    Then 3 Text "The end-to-end encryption platform for modern business" is here
    Then 4 "Features" button is here
    Then 5 "Solutions" button is here
    Then 6 "Pricing" button is here
    Then 7 "How it Works" button is here
    Then 8 "Blog" button is here
    Then 9 "Log In" button is here
    Then 10 "Request Demo" button is here
    Then 11 "Sign up Now" button is here
    And 12 "Learn More" button is here