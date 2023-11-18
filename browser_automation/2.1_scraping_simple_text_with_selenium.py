from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Initialize Chrome options
chrome_options = Options()

# Set various options
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=chrome_options
)

# Now you can use `driver` to navigate and interact with web pages
driver.get("https://www.example.com")

# ... perform actions on the web page ...
time.sleep(15)

# Close the driver
driver.quit()
