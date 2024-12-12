import requests
import pytest
import csv

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"


def get_payloads_from_csv(file_path):
    """Read payloads from a CSV file."""
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        payloads = []
        for row in reader:
            # Convert row to appropriate types
            payload = {
                "firstname": row['firstname'],
                "lastname": row['lastname'],
                "totalprice": int(row['totalprice']),
                "depositpaid": row['depositpaid'] == 'True',
                "bookingdates": {
                    "checkin": row['checkin'],
                    "checkout": row['checkout']
                },
                "additionalneeds": row['additionalneeds']
            }
            payloads.append(payload)
    return payloads


@pytest.mark.parametrize("payload", get_payloads_from_csv("MultipleData.csv"))
def test_create_booking(payload):
    """Test case to create a booking using data from CSV."""
    # --- Step 1: Create a Booking ---
    create_endpoint = f"{BASE_URL}/booking"

    create_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Perform POST request
    create_response = requests.post(create_endpoint, headers=create_headers, json=payload)

    # Validate POST response
    booking_data = create_response.json()
    booking_id = booking_data.get("bookingid")
    assert booking_id, "Booking ID not returned in the response"
    print(f"Created Booking ID: {booking_id}")

