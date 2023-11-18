# Import necessary modules from selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

def get_driver():
    # Initialize an instance of ChromeOptions. This class helps in managing options specific to ChromeDriver.
    chrome_options = Options()

    # Adding various arguments to ChromeOptions to customize the browser's behavior:

    # Disables the infobar that shows messages like "Chrome is being controlled by automated test software".
    chrome_options.add_argument("--disable-infobars")

    # Opens the browser in maximized mode.
    chrome_options.add_argument("--start-maximized")

    # Prevents Chrome from using /dev/shm for shared memory, which can cause crashes in certain environments.
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Disables the sandbox security feature in Chrome. Note: This can make your browser less secure.
    chrome_options.add_argument("--no-sandbox")

    # Disables a Chrome feature that detects automation tools controlling the browser, making automation less detectable.
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # Ignores SSL certificate errors. Useful for testing on sites with self-signed certificates.
    chrome_options.add_argument("--ignore-certificate-errors")

    # Excludes the switch that enables automation, helping to make the browser automation less detectable.
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

    # Initialize the Chrome driver with the specified options.
    # ChromeDriverManager automatically downloads the driver binary and sets its path.
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )
    return driver

# Call the get_driver function to initialize the Chrome WebDriver with the specified options.
driver = get_driver()

# Use the `driver` to navigate to a web page.
driver.get("https://automated.pythonanywhere.com")

# Wait for 15 seconds. This is useful for observing what happens on the browser, especially during testing.
time.sleep(15)

# Close the browser and quit the driver session. This is important to free up system resources and avoid potential leaks.
driver.quit()
