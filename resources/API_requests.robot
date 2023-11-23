*** Settings ***
Library           RequestsLibrary
Library           SeleniumLibrary

*** Keywords ***
Post Request With Json
    [Arguments]    ${url}    ${endpoint}    ${name}    ${job}
    ${BODY}=            Create Dictionary  name=${NAME}  job=${JOB}
    ${RESPONSE}=        POST  ${URL}${ENDPOINT}  json=${BODY}
    [Return]            ${RESPONSE}

Post Request With Json And Without Required Parameter
    [Arguments]    ${url}    ${endpoint}    ${job}
    ${BODY}=            Create Dictionary  job=${JOB}
    ${RESPONSE}=        POST  ${URL}${ENDPOINT}  json=${BODY}
    [Return]            ${RESPONSE}

Get Request
    [Arguments]    ${url}
    ${response}=    Get Request    ${url}
    [Return]        ${response}

Verify Status Code
    [Arguments]    ${response}    ${expected_status}
    Should Be Equal As Numbers    ${response.status_code}    ${expected_status}
