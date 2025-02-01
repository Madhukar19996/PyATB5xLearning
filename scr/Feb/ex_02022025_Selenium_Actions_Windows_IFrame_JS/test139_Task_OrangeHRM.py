import allure
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from allure_commons.types import AttachmentType

@allure.title("OrangeHRM")
@allure.description("Verify  Employment Status of First Terminated employee  ")

def test_web_tables_Employee_Status ():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/hr/web/index.php/auth/login")
    driver.maximize_window()
    #driver.implicitly_wait(10)  # seconds  # implicit wait
    time.sleep(5)

    # Login
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("Hacker@4321")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    # PIM-->Employees list
    driver.find_element(By.XPATH, "//a[@href='/hr/web/index.php/pim/viewPimModule']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//li[@class='oxd-topbar-body-nav-tab --visited']").click()
    time.sleep(3)

    # total rows n a table
    rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//div[@class='oxd-table-card']"))
    print("total number of rows in a table:", rows)


    First_User_Terminated = driver.find_element(By.XPATH, "//div//div[@role='row']").text


    Delete_button_ele= driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-trash']")

    Delete_button_ele.click()

    time.sleep(2)

    allure.attach(driver.get_screenshot_as_png(), name="test_verify_action_makemytrip-screenshot",attachment_type=AttachmentType.PNG)


    driver.close()



