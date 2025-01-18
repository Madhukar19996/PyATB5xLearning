from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os


@allure.title("Demo ESPO_CRM positive Testcase")
@allure.description("TC1 - Positive TC - Verify the Title and current URL.")
@pytest.mark.Positive
def test_verify_title_chrome():
    load_dotenv()
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get(os.getenv("URL_DEMO_ESPO"))
    #print(driver.title)
    assert driver.title=="EspoCRM Demo"
    assert driver.current_url=="https://demo.us.espocrm.com/"

    driver.quit()

@allure.title("Demo ESPO_CRM Positive Testcase")
@allure.description("TC2 - Positive TC - Click on login and verify the current page Url")
@pytest.mark.Positive
def test_verify_login_chrome():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("URL_DEMO_ESPO"))
    time.sleep(5)
    login_button_element = driver.find_element(By.XPATH,"//button[@id='btn-login']")
    login_button_element.click()
    time.sleep(5)
    assert driver.current_url== os.getenv("URL_DEMO_ESPO_LOGIN")

    driver.quit()

@allure.title("Demo ESPO_CRM Positive Testcase")
@allure.description("TC3 - Positive TC - Click on Advance pack link ")
@pytest.mark.adv_pack
def test_click_adv_pack_chrome():
        load_dotenv()
        driver = webdriver.Chrome()
        driver.get(os.getenv("URL_DEMO_ESPO"))
        time.sleep(5)
        adv_pack_link_element = driver.find_element(By.XPATH,
                                                    "//a[@href='https://www.espocrm.com/extensions/advanced-pack/']")
        adv_pack_link_element.click()
        time.sleep(5)
        assert driver.current_url== os.getenv("URL_DEMO_ESPO_ADV_PACK")

        driver.quit()

@allure.title("Demo ESPO_CRM Positive Testcase")
@allure.description("TC4 - Positive TC - Click on Sales pack link ")
@pytest.mark.Positive
def test_click_sales_pack_chrome():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("URL_DEMO_ESPO"))
    time.sleep(5)
    sales_pack_link_element = driver.find_element(By.XPATH, "//a[@href='https://www.espocrm.com/extensions/sales-pack/']")
    sales_pack_link_element.click()
    time.sleep(10)
    assert driver.current_url== os.getenv("URL_DEMO_ESPO_SALES_PACK")

    driver.quit()  # close everything.

@allure.title("Demo ESPO_CRM Positive Testcase")
@allure.description("TC5 - Positive TC - Click on personal demo ")
@pytest.mark.demo_espo_crm
def test_click_personal_demo_chrome():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(os.getenv("URL_DEMO_ESPO"))
    time.sleep(5)
    #<a href="https://www.espocrm.com/cloud-registration/?plan=demo">personal demo</a>
    personal_demo_link_element = driver.find_element(By.XPATH, "//a[@href='https://www.espocrm.com/cloud-registration/?plan=demo']")
    personal_demo_link_element.click()
    time.sleep(8)

    assert driver.current_url==os.getenv("URL_PERSONAL_DEMO")

    driver.quit()



