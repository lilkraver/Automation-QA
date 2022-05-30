#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@Feature
Feature: myFeature
  This is my dummyfeature file

  @Scenario
  Scenario: Calculating with the four basic arithmetic operations
   Given I use the calculator
   When I enter "1" into the calculator
   And I add "200"
   And I subtract "200"
   And I divide by "555"
   And I multiply by "555"
   Then the calculated result is "1"
