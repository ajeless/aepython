from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver_manager = ChromeDriverManager()
driver = webdriver.Chrome(driver_manager.install())

options = webdriver.ChromeOptions()
options.add_argument(
    '--ignore-certificate-errors', 
    '--incognito', 'disable-infobars', 
    'start-maximized', 
    'disable-dev-shm-usage', 
    'no-sandbox')

# driver = webdriver.Chrome()