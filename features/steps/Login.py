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

@given(u'open  HRM browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    s = Service("C:\\Users\\Plabani\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')  #

@when(u'enter valid credental username1 "Admin" and password1 "admin123"')
def step_impl(context):
    driver.find_element("name", 'username').send_keys("Admin")
    driver.find_element("name", 'password').send_keys("admin123")

@when(u'enter valid credental username1 <"username"> and password1 <"password">')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When enter valid credental username1 <"username"> and password1 <"password">')
    driver.find_element("name", 'username').send_keys("Admin")
    driver.find_element("name", 'password').send_keys("admin123")
@then(u'click login button1')
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()
    #driver.find_element("name", 'password').send_keys("admin123")

@then(u'Home page loaded successfully1')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Home page loaded successfully1')
