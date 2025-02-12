import time
from typing import Any

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait


# Mywait = WebDriverWait(driver, 10, poll_frequency=2,
#                            ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
#                                                ElementNotSelectableException, Exception])


def test_web_tables_status():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    driver.implicitly_wait(10)  # seconds  # implicit wait
    # time.sleep(5)

    # Login
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    # time.sleep(3)

    # # Admin-->user management-->users
    driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
    # time.sleep(5)
    driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --parent --visited']").click()

    # time.sleep(3)
    driver.find_element(By.XPATH, "//a[@role='menuitem']").click()
    # time.sleep(3)

    # total rows n a table
    rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@class='oxd-table-card']"))
    print("total number of rows in a table:", rows)

    count = 0
    for r in range(1, rows + 1):
        status = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']//div[" + str(r) + "]//div[5]").text
        if status == "Enabled":
            count = count + 1

    print("Total Number of users:", rows)
    print("Number of enabled users:", count)
    print("Number of disabled users:", (rows - count))

    driver.close()


def test_web_tables():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()
    time.sleep(5)

    # Login
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    # # Admin-->user management-->users
    driver.find_element(By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --parent --visited']").click()

    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@role='menuitem']").click()
    time.sleep(3)

    # total rows n a table
    rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@class='oxd-table-card']"))
    print("total number of rows in a table:", rows)

    count = 0
    for r in range(1, rows + 1):
        user_role = driver.find_element(By.XPATH, "//div[@class='oxd-table-body']//div[" + str(r) + "]//div[3]").text
        if user_role == "ESS":
            count = count + 1

    print("Total Number of users:", rows)
    print("Number of ESS users:", count)
    print("Number of Admin users:", (rows - count))

    driver.close()