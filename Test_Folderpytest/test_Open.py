import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture()
def chk():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    s = Service('C:\Users\Plabani\Downloads\chromedriver-win64 (1)\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=s)

    driver.get("file:///C:/Users/Plabani/Documents/Plabani.html")
    yield
    driver.close()


def test_verify(chk):
    driver.execute_script(("document.getElementById('input1').value='Selenium'"))
    time.sleep(5)
    driver.execute_script(("document.getElementById('input1').value=' '"))


@pytest.mark.skip("skipping")
def test_skp():
    print("display")


'''''
driver.get("https://demowebshop.tricentis.com/login")
driver.maximize_window()
element= driver.find_element("xpath","/html/body/div[4]/div[1]/div[2]/ul[1]/li[2]/a")
actions=ActionChains(driver)
actions.move_to_element(element).perform()
driver.execute_script("window.scrollBy(0,40)")
time.sleep(10)
driver.execute_script("window.scrollBy(0,-40)")
'''''
