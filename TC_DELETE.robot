*** Settings ***
Library    RequestsLibrary
Library    Collections
*** Variables ***

${BASE_URL}    https://restful-booker.herokuapp.com
${BOOKING_ENDPOINT}    /booking
${BOOKING_ID}    1007  # Replace with the actual ID of the booking you want to delete

*** Test Cases ***
Delete Booking with DELETE Method
    # Create a session with Basic Authentication
    ${auth}=    Create List     admin   password123
    Create Session    my_session    ${BASE_URL}    auth=${auth}

    # Make a DELETE request
    ${response}=    Delete Request    my_session    ${BOOKING_ENDPOINT}/${BOOKING_ID}

    # Log the response status code and response body
    Log to console    ${response.status_code}
    Log to console    ${response.text}