import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
import openpyxl

# Path to the Excel file
excel_file = 'C:\\Users\\Plabani\\Documents\\Sound Recordings\\Book3.xlsx'
sheet_name = 'Sheet1'

# Load the credentials from the Excel file
df = pd.read_excel(excel_file, sheet_name=sheet_name)
username = df['username'].iloc[0]  # Fetch the first row's username
password = df['password'].iloc[0]  # Fetch the first row's password

@pytest.fixture()
def test_verifyURL():
    global driver

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(5)


# Example: Using username and password from Excel in a test
def test_login(test_verifyURL):
    driver.find_element("name", "username").send_keys(username)