*** Settings ***
Library    OperatingSystem
Library    String
Library    SeleniumLibrary
Library     Collections


*** Variables ***
${CREDENTIALS_FILE}    C://Users//Plabani//Documents//MY//quick.csv
${URL}      https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
*** Test Cases ***
Data-Driven Login
    ${file_content}=    Get File    ${CREDENTIALS_FILE}
    @{rows}=    Split To Lines    ${file_content}
    @{data_rows}=    Create List    @{rows}[1:]  # Slicing to skip the header
    FOR    ${row}    IN    @{data_rows}
        ${username}    ${password}=    Split String    ${row}    ,
        Log    Username: ${username} | Password: ${password}
        Open Browser    ${URL}    chrome        options= add_experimental_option("detach",True)
        sleep       5s
        Input Text    name=username    ${username}
        Input Text    name=password    ${password}
    END