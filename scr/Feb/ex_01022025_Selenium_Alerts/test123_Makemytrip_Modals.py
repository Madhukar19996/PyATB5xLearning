import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("modals_make_myt_rip.com")
@allure.description("Verify that enter mobile number amd click on Continue Button ")
def test_alerts_js_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")



    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='Enter Mobile Number']")))

    modal = driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile Number']")
    modal.send_keys("9877854321")
    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Continue']")))
    continue_button = driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
    continue_button.click()


time.sleep(5)