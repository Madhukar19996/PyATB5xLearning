from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@allure.title("VWO Login Negative Testcase ")
@allure.description("TC1- Negative Testcase- VWO Login with invalid creds ")
@pytest.mark.negativeVWO_Login
def test_app_vwo_login_chrome():
    load_dotenv()


    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL"))

    #<a
    # href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
    # class="text-link"
    # data-qa="bericafeqo">
    # Start a free trial
    # </a>
    #Link text and Partial text
    # Link Text =Exact Match

    # anchor_element = driver.find_element(By.LINK_TEXT, "Start a free trial")
    # anchor_element.click()
    #
    # assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    #
    #Partial_Link_Text-Contains
    anchor_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_element.click()

    assert driver.current_url=="https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5)
    driver.quit()  # close everything.