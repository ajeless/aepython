# Importing necessary modules and classes from the Selenium package, Python's logging library, and other required libraries.
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from contextlib import contextmanager


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


def log_to_output(msg):
    # Setting up a logger to record messages.
    logger = logging.getLogger(__name__)

    # Setting the log level to INFO, which includes messages of level INFO and above.
    logger.setLevel(logging.INFO)

    # Creating a file handler to write logs to a file.
    handler = logging.FileHandler("my_log.log")

    # Defining the format for log messages.
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # Adding the handler to the logger.
    logger.addHandler(handler)

    # Preventing the log messages from being propagated to higher-level loggers.
    logger.propagate = False

    # Logging the provided message.
    logger.info(f"{msg}")


def main():
    # Using the get_driver context manager to ensure the WebDriver is set up and torn down correctly.
    with get_driver() as driver:
        # Directing the WebDriver to navigate to a specific URL.
        driver.get("https://automated.pythonanywhere.com/login/")

        # Waiting until the username input field is visible.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id_username"))
        )
        # Finding the username input field by its ID and entering text.
        driver.find_element(By.ID, "id_username").send_keys("automated")

        # Waiting until the password input field is visible.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "id_password"))
        )
        # Finding the password input field by its ID and entering text.
        driver.find_element(By.ID, "id_password").send_keys("automatedautomated")

        # Waiting until the submit button is visible.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        # Finding the submit button by its XPATH and clicking it.
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Printing the current URL after logging in.
        print(f"{driver.current_url}")

        # Waiting until the 'Home' link is visible.
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
        )
        # Clicking the 'Home' link.
        driver.find_element(By.LINK_TEXT, "Home").click()

        # Looping 5 times to demonstrate repeated actions on a web page.
        for i in range(5):
            # Using WebDriverWait to wait for a specific element to become visible.
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "#displaytimer .text-success")
                )
            )

            # Finding an element by its CSS selector and storing its text content.
            average_world_temperature = driver.find_element(
                By.CSS_SELECTOR, "#displaytimer .text-success"
            ).text

            # Logging the retrieved text to a file.
            log_to_output(average_world_temperature)

            # Pausing the script for 5 seconds before continuing the loop.
            time.sleep(5)

        # Printing the current URL after completing the actions.
        print(f"{driver.current_url}")


# This conditional statement checks if the script is being run directly (not imported as a module).
# If it is run directly, it calls the main function.
if __name__ == "__main__":
    main()
