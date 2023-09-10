Feature: myfeature
  Scenario: Validate Search feature
    Given Browser is launched
    When I search for required data "DREAM WEAVERZ"
    Then I Verify data is available
    And Close browser

  Scenario: Validate Navigation feature
    Given Browser is launched
    When I select Men from the dropdown
    Then I validate whether proper Page is loaded
    And Close browser

  Scenario: Validate sort feature
    Given Browser is launched
    When I sort by using popularity
    Then I Verify data is available
    Then Close browser

  Scenario: Validate filter feature
    Given Browser is launched
    When I filter by white colour
    Then I validate page is filtered by white colour
    Then Close browser

  Scenario: Validate login phone feature
    Given Browser is launched
    When I move to login page via landing page
    Then I validate login page asks for phone number
    Then Close browser