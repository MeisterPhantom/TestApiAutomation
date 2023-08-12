# Created by ivan at 1/6/23
Feature: Test functional API Neo from NASA
  The API neo from NASA provides information
  For some near objects to earth

  Scenario: Get list objects near earth
    Given the API requires 2022-07-01 and 2022-07-07 data date
    Then the API status code response es equal to 200

  Scenario: Get  lookup asteroid near to earth
    Given the API requires 2465633 asteroid id
    Then the API status code response es equal to 200

  Scenario: Browse all data of asteroids
    Given the API to get all data of asteroids
    Then the API status code response es equal to 200