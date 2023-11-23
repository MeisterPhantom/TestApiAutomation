*** Keywords ***
Base Api
    ${BASE_URL}=    Set Variable    ${BASE_URL}
    log To Console  ${BASE_URL}

*** Variables ***
${BASE_URL}     https://reqres.in/api