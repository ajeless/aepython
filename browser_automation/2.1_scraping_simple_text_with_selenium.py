# Importing necessary modules and classes from the Selenium package and other required libraries.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from contextlib import contextmanager
import time


# Defining a context manager to handle the setup and teardown of the Selenium WebDriver.
@contextmanager
def get_driver():
    # Creating an instance of Options to configure ChromeDriver settings.
    chrome_options = Options()
    # Setting various options to control the behavior of the Chrome browser.
    chrome_options.add_argument("--disable-infobars")  # Disables the infobars.
    chrome_options.add_argument("--start-maximized")  # Starts Chrome maximized.
    chrome_options.add_argument(
        "--disable-dev-shm-usage"
    )  # Overcomes limited resource problems.
    chrome_options.add_argument(
        "--no-sandbox"
    )  # Bypasses OS security model; used in container environments.
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled"
    )  # Disables the flag that shows Chrome is being automated.
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"]
    )  # Excludes the switch that enables automation.

    # Initializing the Chrome WebDriver using ChromeDriverManager.
    # ChromeDriverManager automatically downloads the driver binary and sets its path.
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=chrome_options
    )

    try:
        # Yielding the WebDriver object to the calling function, allowing it to be used outside this context manager.
        yield driver
    finally:
        # Ensuring the WebDriver is closed properly, which closes the browser window and frees up resources.
        driver.quit()


def main():
    # Using the get_driver context manager to ensure the WebDriver is set up and torn down correctly.
    with get_driver() as driver:
        # Directing the WebDriver to navigate to a specific URL.
        driver.get("https://automated.pythonanywhere.com")

        # Looping 10 times to demonstrate repeated actions on a web page.
        for i in range(10):
            # Using WebDriverWait to wait for a specific element to become visible.
            # This is a more robust method compared to static waiting, as it adapts to different loading times.
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#displaytimer .text-success")
                )
            )

            # Finding an element by its CSS selector and printing its text content.
            print(
                driver.find_element(By.CSS_SELECTOR, "#displaytimer .text-success").text
            )
            # Pausing the script for 2 seconds before continuing the loop.
            time.sleep(2)

        # Waiting for an additional 5 seconds at the end of the loop.
        time.sleep(5)


# This conditional statement checks if the script is being run directly (not imported as a module).
# If it is run directly, it calls the main function.
if __name__ == "__main__":
    main()
