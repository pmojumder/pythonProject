
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture()
def test_verifyURL():
    global driver


    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")


def test_clickBooks(test_verifyURL):
    expected_title = "Demo Web Shop"
    actual_title = driver.title
    # Assert that the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}"
    driver.find_element("xpath","(//a[contains(text(),'Books')])[1]").click()
    assert "books" in driver.current_url.lower(), "Failed to navigate to Books page"



@pytest.mark.skip("skipping")
def test_clicklogout(test_verifyURL):
    print("this is just sample one")

@pytest.mark.skip("skipping")
def test_clicklogout1():
    print("this is just sample one")

'''
def test_page_title(driver):
    # Navigate to the webpage
    expected_title = "Demo Web Shop"
    actual_title = driver1.title
    # Assert that the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}
'''