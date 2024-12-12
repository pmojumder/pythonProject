
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

    driver.get("https://demowebshop.tricentis.com/")



def test_clickBooks(test_verifyURL):
     driver.find_element("xpath","(//a[contains(text(),'Books')])[1]").click()
'''
@pytest.mark.skip("skipping")
def test_clicklogout():
    print("this is just sample one")
'''