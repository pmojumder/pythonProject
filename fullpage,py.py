from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import time

# Function to take a full page screenshot
def take_full_page_screenshot(driver, screenshot_path):
    # Execute a command to capture full page screenshot
    driver.get(screenshot_path)
    # Save full-page screenshot (scrolls down and takes a full capture)
    screenshot_path = 'C:\\Users\\Plabani\\Documents\\MYfull_page_screenshot.png'
    driver.save_screenshot(screenshot_path)

    return screenshot_path

# Function to add a date stamp on the image
def add_date_stamp(image_path):
    # Open the screenshot using Pillow
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Get current date and time
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Set font, either specify the font or default one
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except IOError:
        font = ImageFont.load_default()

    # Position for the date stamp
    text_position = (10, 10)

    # Add the date stamp
    draw.text(text_position, current_time, font=font, fill="white")

    # Save the new image with a date stamp
    stamped_image_path = "full_page_screenshot_with_date.png"
    img.save(stamped_image_path)

    print(f"Screenshot with date stamp saved as {stamped_image_path}")

    return stamped_image_path


# Set up Chrome WebDriver with options for full-page screenshot
options = Options()
options.add_argument("--start-maximized")  # Start with max window size
options.add_argument("--headless")         # Optional: Run headlessly (no GUI)

# Path to chromedriver
chromedriver_path = "C:\\Users\\Plabani\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe"  # Replace with your chromedriver path
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open the webpage you want to capture
driver.get('https://mvnrepository.com/artifact/commons-io/commons-io/2.18.0')  # Replace with the URL you want

# Ensure the page is fully loaded
time.sleep(2)

# Take a full page screenshot
screenshot_path = take_full_page_screenshot(driver, 'screenshot')

# Close the driver
driver.quit()

# Add date stamp to the screenshot
add_date_stamp(screenshot_path)
