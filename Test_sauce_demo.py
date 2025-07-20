import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)

# to check webpage title and URL
def test_title_and_url():
    driver.get("https://www.saucedemo.com")
    #  Checks title
    if "Swag Labs" in driver.title:
        print("Swag Labs found in Title.Title verified.")
    else:
        print("Swag Labs not found in title.Testcase failed")

    #  Checks URL
    if driver.current_url == "https://www.saucedemo.com/":
        print("URL of the Homepage. test passed.")
    else:
        print("URL of the Homepage is incorrect. test failed.")

# Positive testcase with correct login details
def test_postive_login_valid():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url,"inventory is not in url"
    print("Login Successfull")

# Negative testcase with incorrect password
def test_negative_login_invalid_1():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    if "Epic sadface" in error:
        print("Invalid login test passed.")
    else:
        print("Invalid login test failed.")

# Negative testcase with incorrect login
def test_negative_login_invalid_2():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("Stand_use")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    if "Epic sadface" in error:
        print("Invalid login test passed.")
    else:
        print("Invalid login test failed.")

# Negative testcase with Blank login and password
def test_negative_login_invalid_3():
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys(" ")
    driver.find_element(By.ID, "password").send_keys(" ")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    if "Epic sadface" in error:
        print("Invalid login test passed.")
    else:
        print("Invalid login test failed.")


