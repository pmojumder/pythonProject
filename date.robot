*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.makemytrip.com/
${DEPARTURE_DATE}    2024-10-10
${RETURN_DATE}    2024-10-20

*** Test Cases ***
Select Dates From Dynamic Datepicker
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    sleep   15s
    Wait Until Element Is Visible    xpath=//span[text()='Departure']
    Click Element    xpath=//span[text()='Departure']
    Select Date    ${DEPARTURE_DATE}
    Click Element    xpath=//span[text()='RETURN']
    Wait Until Element Is Visible    xpath=//span[text()='Return']
    Click Element    xpath=//span[text()='Return']
    Select Date    ${RETURN_DATE}
    Close Browser

*** Keywords ***
Select Date
    [Arguments]    ${date}
    ${year}    Set Variable    ${date}[0:4]
    ${month}   Set Variable    ${date}[5:7]
    ${day}     Set Variable    ${date}[8:10]

    # Open the calendar if necessary
    Click Element    xpath=//input[@data-cy='departure']  # Using data-cy attribute

    # Wait for the date picker to be visible
   # Wait Until Element Is Visible    xpath=//div[contains(@class, 'datePickerContainer')]

    FOR    ${i}    IN RANGE    12
        ${current_month_year}    Get Text    xpath=//div[contains(@class, 'datePickerContainer')]
        ${month_year}    Split String    ${current_month_year}    ${SPACE}
        ${displayed_month}    Set Variable    ${month_year}[0]
        ${displayed_year}    Set Variable    ${month_year}[1]

        Log    Current displayed month/year: ${displayed_month} ${displayed_year}
        Run Keyword If    '${displayed_month}'=='${month}' and '${displayed_year}'=='${year}'    Exit For Loop
        Click Element    xpath=//span[@aria-label='Next Month']
    END

    # Click the specific date using JavaScript to avoid click interception
    Execute JavaScript    arguments[0].click();    xpath=//div[@aria-label='${day} ${month} ${year}']
