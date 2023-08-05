from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options

def open_browser(url, incognito=False, headless=False):
    service = Service("C:/Users/Amogh/Desktop/selenium_framework/Constants/driver/chromedriver.exe")
    chrome_options = Options()
    if incognito:
        chrome_options.add_argument("--incognito")
        
    if headless:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    return driver

def enter_text_in_element(driver , xpath , text):
    wait_until_element_is_visible(driver , xpath , wait_time=10)
    element = driver.find_element(By.XPATH, xpath)
    element.send_keys(text)


def click_element(driver, xpath):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

#### ALL EXCEPTION HANDELING GOES HERE ####

# explicit wait time
def wait_until_element_is_visible(driver, xpath, wait_time=10):
    wait = WebDriverWait(driver, wait_time)
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if element:
            return f"Element found: {xpath}."
    except Exception as e:
        print(f"{e}: Element not found: {xpath}.")
        # raise Exception