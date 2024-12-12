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



@given(u'open orange HRM browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    s = Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

'''
@when(u'enter valid credental username "{user}" and password "{password}"')
def step_impl(context, user, password):
    driver.find_element("name", "username").send_keys(user)
    driver.find_element("name", "password").send_keys(password)
'''

@then(u'click login button')
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()


@then(u'Home page loaded successfully')
def step_impl(context):
    print(driver.title)

@when(u'enter username {username} and {password}')
def step_impl(context,username,password):
   driver.find_element("name","username").send_keys(config.read("config.ini",username))
   driver.find_element("name","password").send_keys(password)





@given(u'click admin buttpn')
def step_impl(context):
    driver.find_element("xpath", "//span[text()='PIM']").click()


@given(u'click Add button')
def step_impl(context):
    driver.find_element("xpath", "//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
