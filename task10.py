from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Initialize Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)

try:
    # Open the website
    driver.get("https://www.saucedemo.com/")

    # Login with provided credentials
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)

    # 1. Get title of the webpage
    title = driver.title
    print("Title of the webpage:", title)

    # 2. Get current URL
    current_url = driver.current_url
    print("Current URL:", current_url)

    # 3. Save entire page content to text file
    Page_contents=driver.find_element(By.XPATH, "//html/body").text
    with open("Webpage_task_11.txt", "w", encoding='utf-8') as file:
        file.write(Page_contents)

    # 4. Save full page source to a file
    with open("Webpage_task_1.txt", "w", encoding='utf-8') as file:
        file.write(driver.page_source)

finally:
    # Always close the browser
    driver.quit()

