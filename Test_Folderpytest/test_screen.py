import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


@pytest.fixture()


def driver():
    global driver1
    # Set up WebDriver
    options = webdriver.ChromeOptions()
    service = Service("C:\\Users\\Plabani\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")  # Update the path to your chromedriver
    driver1 = webdriver.Chrome(service=service, options=options)
    driver1.maximize_window()



def test_example(driver):
    try:
        driver1.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(4)
        # Test steps
        username = driver1.find_element("name", "username")
        username.send_keys("Admin")
        password = driver1.find_element("name", "password")
        password.send_keys("wrongpassword")
        login_button = driver1.find_element("xpath", "//button[@type='submit']")
        login_button.click()

        # Assertion
        assert "dashboard" in driver1.current_url.lower()  # Fails if login is invalid

    except AssertionError:
        # Take a screenshot if the test fails

        screenshot_path = "C:\\Users\\Plabani\\Downloads\\Performance\\planami.png"
        driver1.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
        raise  # Re-raise the exception to mark the test as failed
