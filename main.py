import keyring as kr
import getpass
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

SERVICE_NAME = 'amazon-photos-uploader'
AMAZON_URL = 'https://www.amazon.it/photos'
XPATH_GET_STARTED = '//a[text()="Accedi"]'

def get_driver(browser_choice):

    driver = None
    
    print("Waiting for the driver to load...")
    sys.stdout.flush() 

    if browser_choice.lower() == 'chrome':
        driver = webdriver.Chrome()
    
    elif browser_choice.lower() == 'firefox':
        driver = webdriver.Firefox()
    
    elif browser_choice.lower() == 'edge':
        driver = webdriver.Edge()
    
    if driver == None:
        print("Browser not supported. Choose Chrome, Firefox or Edge.")
    else:
        print("\rDriver loaded, proceeding with the rest of the program...")

    return driver

def get_inputs():

    email = None
    pwd = None
    browser = kr.get_password(SERVICE_NAME, "browser")

    email = input("email: ")
        
    pwd = kr.get_password(SERVICE_NAME, email)

    if pwd == None:

        pwd = getpass.getpass("password: ")

        remember = input(("remember? [Y/n] "))
        if remember == "y" or remember == "Y":
            kr.set_password(SERVICE_NAME, email, pwd)

    if browser == None:
        browser = input("browser: [chrome, firefox or edge] ")
        kr.set_password(SERVICE_NAME, "browser", browser)

    return email, pwd, browser

def login(driver, email, password):

    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ap_email"))
    )
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "ap_password"))
    )
    password_input.send_keys(password)

    login_button = driver.find_element(By.ID, "signInSubmit")
    login_button.click()


def main():

    email, pwd, browser = get_inputs()

    driver = get_driver(browser)
    
    if driver == None:
        exit(1)

    driver.get(AMAZON_URL)

    try:
        get_started_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, XPATH_GET_STARTED))
        )

        get_started_btn.click()

    except Exception as e:
        print("Error while trying to click 'get started button'", e)

    login(driver, email, pwd)

    input()