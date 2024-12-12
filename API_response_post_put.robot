*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${BASE_URL}        https://restful-booker.herokuapp.com
${BOOKING_ENDPOINT}     /booking
${CONTENT_TYPE}    application/json

*** Test Cases ***
Test Case to Create and Update a Booking
    # Create a session with Basic Authentication
    ${auth}=    Create List    admin    password123
    Create Session    my_session    ${BASE_URL}    auth=${auth}

    ${headers}=    Create Dictionary    Content-Type=${CONTENT_TYPE}
    ${bookingdates}=    Create Dictionary    checkin=2024-08-26    checkout=2024-08-27
    ${body}=    Create Dictionary    firstname=Plabani    lastname=M    totalprice=190    depositpaid=True    bookingdates=${bookingdates}    additionalneeds=Breakfast

    # Make a POST request to create a booking
    ${response}=    POST Request    my_session    ${BOOKING_ENDPOINT}    json=${body}    headers=${headers}

    # Log the response
    Log to console    ${response.status_code}
    Log to Console    ${response.json()}

    # Extract Booking ID from the response
    ${booking_id}=    Get From Dictionary    ${response.json()}    bookingid
    Log to Console    Booking ID: ${booking_id}

    # Prepare data for PUT request
    ${updated_bookingdates}=    Create Dictionary    checkin=2024-09-01    checkout=2024-09-02
    ${update_body}=    Create Dictionary    firstname=Plabani    lastname=M    totalprice=200    depositpaid=True    bookingdates=${updated_bookingdates}    additionalneeds=Dinner

    # Make a PUT request to update the booking
    ${update_response}=    PUT Request    my_session    ${BOOKING_ENDPOINT}/${booking_id}    json=${update_body}    headers=${headers}

    # Log the response of the PUT request
    Log to Console    ${update_response.status_code}
    Log to Console    ${update_response.json()}

    ${log_getresponse}=    get request     my_session        ${BOOKING_ENDPOINT}/${booking_id}
    log to console     ${log_getresponse.status_code}
    log to console     ${log_getresponse.content}