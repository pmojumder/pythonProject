
*** Settings ***
Library    OperatingSystem
Library    BuiltIn
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}    https://restful-booker.herokuapp.com
${BOOKING_ENDPOINT}    /booking
${CONTENT_TYPE}    application/json
${JSON_FILE_PATH}    C:/Users/Plabani/PycharmProjects/pythonProject/API_DATADRIVEN.json

*** Test Cases ***
Create Booking with Data from JSON File
    # Create a session with Basic Authentication
    ${auth}=    Create List     admin   password123

    Create Session    my_session    ${BASE_URL}    auth=${auth}

    # Read the JSON file
    ${file_content}=    Get File    ${JSON_FILE_PATH}

    # Parse the JSON content
    ${body}=    Evaluate    json.loads('''${file_content}''')    modules=json

    # Prepare headers
    ${headers}=    Create Dictionary    Content-Type=${CONTENT_TYPE}

    # Make a POST request with the data from the JSON file
    ${response}=    Post Request    my_session    ${BOOKING_ENDPOINT}    json=${body}    headers=${headers}

    # Log the response status code and response body
    Log to console    ${response.status_code}
    Log to console    ${response.text}