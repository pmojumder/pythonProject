import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\Plabani\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.implicitly_wait(5)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()
#driver.find_element("id","fn").send_keys("Plabani")
clickable_element = WebDriverWait(driver, 10)
#clickable_element.until(
 #   EC.frame_to_be_available_and_switch_to_it(("xpath", "//iframe[@id='frm']"))
  #  )
#clickable_element.until(EC.alert_is_present())
clickable_element.until(EC.title_contains("OrangeM"))
print("Action not Completed")
#driver.find_element("id","mn").send_keys("M")
#driver.switch_to.default_content()
#driver.switch_to.parent_frame()
#driver.find_element("id","ln").send_keys("n")

driver.implicitly_wait(5)


print("Element is clickable!")
# clickable_element.click()  # Interact with the element once it is clickable

'''
driver.save_screenshot("C:\\Users\\Plabani\\Downloads\\Performance\\planami.png")

driver.execute_script("window.scrollBy(0, 1000);")
driver.execute_script("window.scrollBy(0, -1000);")

driver.maximize_window()
time.sleep(4)

a=ActionChains(driver)
element=driver.find_element("xpath","//button[text()='Double-Click Me To See Alert']")
a.double_click(element).perform()
alert=Alert(driver)

time.sleep(4)
print(alert.text)
alert.accept()

#alert.dismiss()


elementsource=driver.find_element("xpath","//img[@alt='The peaks of High Tatras']")
elementtarget=driver.find_element("xpath","//div[@class='ui-widget-content ui-state-default ui-droppable']")

a=ActionChains(driver)

#a.move_to_element(element).perform()
#a.context_click(element).perform()
a.drag_and_drop(elementsource,elementtarget).perform()

x=driver.find_element("xpath","(//select[@class='spTextField'])[1]")
sel=Select(x)
time.sleep(4)
sel.select_by_index(2)
time.sleep(2)

sel.select_by_index(3)
sel.deselect_all()
#sel.select_by_index(4)

#sel.select_by_value("https://demowebshop.tricentis.com/books?orderby=6")

sel.select_by_visible_text("Created on")




xyz=driver.find_element("partial link text","Register")
print(xyz.text)
print(xyz.tag_name)
xyz.click()

#element=driver.find_element("partial link text","Register")
#print(element.tag_name)
#element.click()

print(driver.title)
print(driver.current_url)
time.sleep(4)

driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(4)
driver.find_element("xpath","//span[text()='Admin']").click()

driver.find_element("xpath","//input[@name='username']").send_keys("Admin")
driver.find_element("xpath","//input[@name='password']").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()
'''