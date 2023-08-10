
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


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
    element.clear()
    element.send_keys(text)


def click_element(driver, xpath):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def hover_over_on_element(driver, xpath):
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

def handle_alert(driver , accept=True):
    alert = Alert(driver)
    txt_message = alert.text
    if accept:
        alert.accept()
    else:
        alert.dismiss()
    
    return txt_message

#### ALL EXCEPTION HANDELING GOES HERE ####

# explicit wait time
def wait_until_element_is_visible(driver, xpath, wait_time=30):
    wait = WebDriverWait(driver, wait_time)
    try:
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        if element:
            return f"Element found: {xpath}."
    except Exception as e:
        print(f"{e}: Element not found: {xpath}.")
        # raise Exception