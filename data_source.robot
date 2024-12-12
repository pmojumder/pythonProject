*** Settings ***
Library           DataDriver
Suite Setup       Open Browser And Navigate To Login Page
Suite Teardown    Close Browser

*** Test Cases ***
Login With Different Users
    [DataSource]    C:/Users/Plabani/Documents/MY/Plabani.xlsx
    [Variables]    ${Username}    ${Password}
    Login Test    ${Username}    ${Password}