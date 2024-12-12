*** Settings ***
Library     SeleniumLibrary
Library     DateTime

*** Variables ***
${browser}  chrome
${url}      https://demowebshop.tricentis.com/books
${arg}      options= add_experimental_option("detach",True)
${SCREENSHOT_DIR}   C:/Users/Plabani/Documents/MY/
${USERNAME}    admin
${PASSWORD}    admin123
*** Test Cases ***
LoginTest
    [tags]      priority=2
    SeleniumLibrary.Open Browser        https://www.google.com/      ${browser}       options= add_experimental_option("detach",True)
New
    [tags]      priority=1
    SeleniumLibrary.Open Browser        ${url}      ${browser}       options= add_experimental_option("detach",True)
    SeleniumLibrary.Maximize Browser Window
    sleep   3s
    #Open Browser    ${URL}    ${BROWSER}
    ${timestamp}=    Get Current Date    result_format=%Y-%m-%d_%H-%M-%S
    # Define screenshot filename with timestamp
    ${filename}=    Set Variable    ${SCREENSHOT_DIR}screenshot_${timestamp}.png
    # Capture a screenshot
    Capture Page Screenshot    ${filename}
    # Close the browser
    #Close Browser
    #Select From List By Index       name:products-orderby   3
    #input text      name:cusid     123
    #click element       name:submit
    #alert should be present     Do you really want to delete this Customer?
    #${alert_text}=      Execute JavaScript  return window.alertMessage
    #Log     ${alert_text}
    #Handle Alert    action=Accept
    #Loginapplication
    #sleep   3s
   # ${title}=   Get Title
    #Log     ${title}
    #Mouse Over      xpath:(//a[contains(text(),'Computers')])[1]



*** Keywords ***
#Loginapplication
   # Input Text  name:username   ${USERNAME}
    #Input Text  xpath://input[@name='password']     ${PASSWORD}
    #Click Button    xpath://button[@type='submit']