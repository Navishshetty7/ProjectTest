Feature: myfeature
  Scenario: Validate login and create order feature
    Given Browser is launched and logged using super admin
    When I select a company of company id "6495e98a860daf001c837627"
    When I impersonate a user
    When I Select create "Dumpster" order
    When I go to billing tab and search for the above order in invoices
#    Then I Verify data is available
    #Then Close browser
#
#  Scenario: Validate Navigation feature
#    Given Browser is launched
#    When I select Men from the dropdown
#    Then I validate whether proper Page is loaded
#    And Close browser
#
#  Scenario: Validate sort feature
#    Given Browser is launched
#    When I sort by using popularity
#    Then I Verify data is available
#    Then Close browser
#
#  Scenario: Validate filter feature
#    Given Browser is launched
#    When I filter by white colour
#    Then I validate page is filtered by white colour
#    Then Close browser
#
#  Scenario: Validate login phone feature
#    Given Browser is launched
#    When I move to login page via landing page
#    Then I validate login page asks for phone number
#    Then Close browser