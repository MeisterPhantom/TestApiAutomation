# Created by ivan at 1/6/23
Feature: Test functional API Neo from NASA
  The API neo from NASA provides information
  For some near objects to earth

  Scenario: Get list objects near earth
    # Enter steps here
  Given the API requires "2022-07-01" and "2022-07-07" data date
    Then the API status code response es equal to "200"