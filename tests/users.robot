*** Settings ***
Resource    ${CURDIR}/../resources/config.robot
Resource    ${CURDIR}/../steps/users/resource_users.robot

Library     SeleniumLibrary

Suite Setup    Base Api

*** Test Cases ***
Create User
    Given The API Is Available
    When A POST Request Is Sent To ${BASE_URL}, ${USERS_ENDPOINT} With ${NAME}, ${JOB} Data
    Then The Status Code Should Be 201
    And The Response Contains ${NAME} And ${JOB} Data
    And The Id Must Be A Positive Integer

Create User With One Data Parameter In Null
    Given The API Is Available
    When A POST Request Is Sent To ${BASE_URL}, ${USERS_ENDPOINT} With ${EMPTY_NAME}, ${JOB} Data
    Then The Status Code Should Be 201
    And The Response Contains ${EMPTY_NAME} And ${JOB} Data
    And The Id Must Be A Positive Integer

Create User Without Required Parameter
    Given The API Is Available
    When A POST Request Is Sent To ${BASE_URL}, ${USERS_ENDPOINT}, ${JOB} Data
    Then The Status Code Should Be 201
    And The Response Contains ${JOB} Data
    And The Id Must Be A Positive Integer

*** Variables ***
${EMPTY_NAME}       Null
${NAME}     Ivan
${JOB}      Ingeniero
${USERS_ENDPOINT}   /users