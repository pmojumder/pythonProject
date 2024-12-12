from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Dates to select
departure_date = "2024-10-10"
return_date = "2024-10-20"

# Convert dates to the required format
departure_day = datetime.strptime(departure_date, "%Y-%m-%d").day
departure_month = datetime.strptime(departure_date, "%Y-%m-%d").strftime("%B")
departure_year = datetime.strptime(departure_date, "%Y-%m-%d").year

return_day = datetime.strptime(return_date, "%Y-%m-%d").day
return_month = datetime.strptime(return_date, "%Y-%m-%d").strftime("%B")
return_year = datetime.strptime(return_date, "%Y-%m-%d").year

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/")
driver.maximize_window()

# Wait for the Departure element and click
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Departure']"))).click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'datePickerContainer')]")))

# Function to select date
def select_date(day, month, year):
    while True:
        current_month_year = driver.find_element(By.XPATH, "//div[contains(@class, 'datePickerContainer')]//h2").text
        displayed_month, displayed_year = current_month_year.split()

        if displayed_month == month and str(year) == displayed_year:
            # Use JavaScript to click the date element
            date_element = driver.find_element(By.XPATH, f"//div[@aria-label='{day} {month} {year}']")
            driver.execute_script("arguments[0].click();", date_element)
            break
        else:
            # Click Next Month
            driver.find_element(By.XPATH, "//span[@aria-label='Next Month']").click()

# Select Departure Date
select_date(departure_day, departure_month, departure_year)

# Select Return Date
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='RETURN']"))).click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'datePickerContainer')]")))
select_date(return_day, return_month, return_year)

# Close the browser
driver.quit()
