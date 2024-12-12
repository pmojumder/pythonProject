import pytest
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# Function to read data from CSV
def read_csv(file_path):
    return pd.read_csv(file_path)


# Fixture to set up the WebDriver
@pytest.fixture(scope="module")
def browser():
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# Function to provide data for parameterized tests
@pytest.fixture(scope="module")
def login_data():
 return read_csv('C:\\Users\\Plabani\\Documents\\MY\\Book2.csv')


# Parametrized test function for login
@pytest.mark.parametrize("username,password,expected_result", [
("Admin", "admin123", "success")
])
def test_login(browser, username, password, expected_result):
# Find and interact with login elements
 driver.find_element("name", 'username').clear()
 driver.find_element("name", 'username').send_keys(username)
 driver.find_element("name", 'password').clear()
 driver.find_element("name", 'password').send_keys(password)
