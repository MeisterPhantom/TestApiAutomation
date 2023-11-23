*** Settings ***
Resource    ${CURDIR}/../../resources/API_requests.robot
Library     SeleniumLibrary
Library     Collections

*** Keywords ***
The API Is Available
    Log To Console  Start the request

A POST Request Is Sent To ${BASE_URL}, ${USERS_ENDPOINT} With ${NAME}, ${JOB} Data
    Set Test Variable    ${NAME_REQ}    ${NAME}
    ${RESPONSE}=    Post Request With Json    ${BASE_URL}    ${USERS_ENDPOINT}    ${NAME}    ${JOB}
    Set Test Variable    ${RESPONSE_VAR}    ${RESPONSE}

A POST Request Is Sent To ${BASE_URL}, ${USERS_ENDPOINT}, ${JOB} Data
    ${RESPONSE}=    Post Request With Json And Without Required Parameter    ${BASE_URL}    ${USERS_ENDPOINT}    ${JOB}
    Set Test Variable    ${RESPONSE_VAR}    ${RESPONSE}

The Status Code Should Be ${CODE_EXPECTED}
    Verify Status Code  ${RESPONSE_VAR}  ${CODE_EXPECTED}

The Response Contains ${NAME_R} And ${JOB_R} Data
    ${NAME_R}=  Get From Dictionary    ${RESPONSE_VAR.json()}       name
    BuiltIn.Should Be Equal As Strings      ${NAME_R}       ${NAME_REQ}
    ${JOB_R}=  Get From Dictionary       ${RESPONSE_VAR.json()}      job
    BuiltIn.Should Be Equal As Strings      ${JOB_R}        ${JOB}

The Response Contains ${JOB-R} Data
    ${JOB_R}=  Get From Dictionary       ${RESPONSE_VAR.json()}      job
    BuiltIn.Should Be Equal As Strings      ${JOB_R}        ${JOB}

The Id Must Be A Positive Integer
    ${ID}=  Get From Dictionary     ${RESPONSE_VAR.json()}     id
    #Should Be Integer       ${ID}
    Should Be True    ${ID} > 0