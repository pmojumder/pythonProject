import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

# Mark a test as "smoke"
@pytest.mark.smoke
@pytest.fixture()
def driver():
    global driver1

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe')
    driver1 = webdriver.Chrome(options=options, service=s)
    driver1.maximize_window()
    driver1.get("https://demowebshop.tricentis.com/")
    time.sleep(5)

# Test marked with "smoke"
@pytest.mark.smoke


def test_clickBooks(driver):
    driver1.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()
    assert "books" in driver1.current_url.lower(), "Failed to navigate to Books page"


# Test marked with "regression"
@pytest.mark.regression
def test_clickComputers(driver):
    driver1.find_element("xpath", "(//a[contains(text(),'Computers')])[1]").click()

# Test marked with "regression" and "login"
@pytest.mark.regression
@pytest.mark.login
def test_login(driver):
    driver1.find_element("xpath", "//a[contains(text(),'Log in')]").click()

# Test marked with "skip" to indicate it's a test to skip
@pytest.mark.skip
def test_clickLogout():
    print("This test is skipped.")

