from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\Plabani\\Downloads\chromedriver-win64 (16)\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://stackoverflow.com/questions/68543285/chrome-browser-closes-immediately-after-loading-from-selenium")