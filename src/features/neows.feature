# Created by ivan at 30/5/23
Feature: Near Earth Object API answer
  As an application developer,
  I want to review the endpoints for the project NeoWS for the NASA

  Scenario: Consult the list of the Near Earth Objects.
    Given the NeoWS API required the start date "2015-09-01" and end date "2015-09-07" data
    Then the response status code is "200"
