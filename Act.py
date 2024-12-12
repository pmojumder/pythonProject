import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_experimental_option("detach", True)
s = Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=s)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()
driver.find_element("xpath","//span[text()='PIM']").click()
driver.find_element("xpath","//button[@class='oxd-button oxd-button--medium oxd-button--secondary']").click()
driver.find_element("xpath","//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']").send_keys("C:\\Users\\Plabani\\Documents\\MY\\chk7.png")


#driver.find_element("name","cusid").send_keys(123)
#driver.find_element("name","submit").click()
#a=Alert(driver)
'''
try:
    element = WebDriverWa it(driver, 10).until(
v+++    EC.url_contains("https://demo.guru99"))
    print("url loaded")
except:
    print("webpage not loaded")


driver.execute_script("window.scrollBy(0,500)")
time.sleep(3)
driver.execute_script("window.scrollBy(0,-500)")


#driver.save_screenshot("C:\\Users\\Plabani\\Documents\\MY\\DEMO\\screen.jpeg")
S1=lambda  X:driver.execute_script("return document.body.parentNode.scroll"+X)
driver.set_window_size(S1('Width'),S1('Height'))
driver.find_element("tag name","body").screenshot("C:\\Users\\Plabani\\Documents\\MY\\chk7.png")


try:
    element = WebDriverWait(driver, 10).until(
        EC.title_contains("orange"))
    print("found")
except:
    print("not found")


driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=2463491726286621147&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062011&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1")
S1=lambda  X:driver.execute_script("return document.body.parentNode.scroll"+X)
driver.set_window_size(S1('Width'),S1('Height'))
driver.find_element("tag name","body").screenshot("C:\\Users\\Plabani\\Documents\\MY\\chk5.png")

driver.get("file:///C:/Users/Plabani/Documents/MY/Page1.html")
driver.find_element("id","fn").send_keys("Alpha")
driver.switch_to.frame(0)
driver.find_element("id","mn").send_keys("M")
driver.switch_to.default_content()
driver.find_element("id","ln").send_keys("K")

driver.find_element("name","cusid").send_keys(123)
driver.find_element("name","submit").click()
a=Alert(driver)
print(a.text)
a.accept()
#a.dismiss()








dropdown1=driver.find_element("id","slv")
sel1=Select(dropdown1)


driver.maximize_window()
time.sleep(5)

sel1.select_by_index(2)
sel1.select_by_index(3)
time.sleep(5)
sel1.deselect_all()

dropdown1=driver.find_element("id","products-orderby")
sel1=Select(dropdown1)
sel1.select_by_visible_text("Price: Low to High")
#sel1.select_by_index(3)
#sel1.select_by_value("https://demowebshop.tricentis.com/books?orderby=5")
#select by index
#select by visible text
#select by value




#driver.find_element("link text","Log in").click()
#driver.find_element("partial link text","Register").click()














#driver.find_element("name","username").send_keys("Admin")
driver.find_element("xpath","//input[@placeholder='Username']").send_keys("Admin")
driver.find_element("xpath","//input[@type='password']").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()
print(driver.title)
time.sleep(5)

driver.find_element("xpath","//span[text()='Admin']").click()
#driver.find_element("name","password").send_keys("admin123")

print(driver.title)
print(driver.current_url)
print(driver.page_source)
driver.close()// parent tab
driver.quit()// child tab



time.sleep(10)
driver.execute_script("window.scrollBy(0,100)")
time.sleep(10)
driver.execute_script("window.scrollBy(0,-100)")
'''
