import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Modals ")
@allure.description("Verify Modals")
def test_alerts_js_alert_normal():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")



    WebDriverWait(driver=driver, timeout=3).until(EC.visibility_of_element_located((By.XPATH,"//span[@class='commonModal__close']")))

    modal = driver.find_element(By.XPATH, "//span[@class='commonModal__close']")

    modal.click()




    time.sleep(5)









