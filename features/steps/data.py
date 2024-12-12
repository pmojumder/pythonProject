from behave import given, when, then
from selenium import webdriver
from config_reader import get_credentials
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser

@given('I am on the login page')
def step_given_on_login_page(context):
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')  # Replace with your login URL

@when('I enter valid credentials')
def step_when_enter_valid_credentials(context):
    username, password = get_credentials()
    driver.find_element("name",'username').send_keys(username)
    driver.find_element("name",'password').send_keys(password)
    #context.browser.find_element_by_id('loginButton').click()  # Replace with your login button id

@then('I should see the homepage')
def step_then_see_homepage(context):
    assert "Home Page" in context.browser.title  # Replace with a condition to verify successful login
    driver.quit()