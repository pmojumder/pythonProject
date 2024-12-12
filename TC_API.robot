*** Settings ***

Library     RequestsLibrary
Library     RequestsLibrary
*** Variables ***

${base_url}     https://restful-booker.herokuapp.com


*** Test Cases ***
TestVerify
        create session      myss      ${base_url}
        ${log_response}=    get request     myss        /booking
        log to console     ${log_response.status_code}
        log to console    ${log_response.content}


