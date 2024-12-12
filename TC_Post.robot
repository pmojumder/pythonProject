*** Settings ***
Library    RequestsLibrary
Library    Collections
Library  RequestsLibrary
Library     Collections
*** Variables ***
${BASE_URL}    https://restful-booker.herokuapp.com
${BOOKING_ENDPOINT}    /booking
${CONTENT_TYPE}    application/json

*** Test Cases ***
Test Case to Create a New Booking with Basic Authentication
    # Create a session with Basic Authentication
    ${auth}=    Create List     admin   password123
    Create Session    my_session    ${BASE_URL}     auth=${auth}

   ${headers}=    Create Dictionary    Content-Type=${CONTENT_TYPE}
    ${bookingdates}=    Create Dictionary    checkin=2024-08-26    checkout=2024-08-27
    ${body}=    Create Dictionary    firstname=Plabani    lastname=M    totalprice=190    depositpaid=True    bookingdates=${bookingdates}    additionalneeds=Breakfast

    # Make a POST request with valid payload
    ${response}=    POST Request    my_session    ${BOOKING_ENDPOINT}    json=${body}    headers=${headers}
    # Make a POST request

    # Log the response
    Log to console      ${response.status_code}
    Log to Console       ${response.json()}