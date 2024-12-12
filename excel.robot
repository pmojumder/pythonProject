Copy code
*** Settings ***
Library           SeleniumLibrary
Library           DataDriver
Suite Setup       Open Browser And Navigate To Login Page
Suite Teardown    Close Browser
*** Test Cases ***
Login With Different Users
    [DataDriver]     C:/Users/Plabani/Documents/MY/Plabani.xlsx
    [Variables]    ${Username}    ${Password}
    Login Test     ${Username}    ${Password}

*** Keywords ***
Open Browser And Navigate To Login Page
    Open Browser    https://opensource-demo.orangehrmlive.com/web/index.php/auth/login    chrome     options= add_experimental_option("detach",True)
    Maximize Browser Window

Login Test
    [Arguments]    ${Username}    ${Password}
    Input Text    name=username    ${Username}
    Input Text    name=password    ${Password}
    # Add assertions to verify login success

Close Browser
    Close All Browsers