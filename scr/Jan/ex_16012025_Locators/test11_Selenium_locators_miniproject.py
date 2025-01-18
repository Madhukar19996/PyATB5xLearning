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

    # 1.Find the Email and enter the wrong username or email
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    # id="login-username"
    # data-qa="hocewoqisi"
    # >
    email_element = driver.find_element(By.ID, "login-username")
    email_element.send_keys(os.getenv("INVALID_USERNAME"))

   #<input
    # type="password"
    # class="text-input W(100%)"
    # name="password"
    # id="login-password"
    # data-qa="jobodapuxe"
    # data-gtm-form-interact-field-id="2"
    # >

    password_element = driver.find_element(By.NAME, "password")
    password_element.send_keys(os.getenv("INVALID_PASSWORD"))

    # <button type="submit"
    # id="js-login-btn"
    # class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)"
    # onclick="login.login(event)"
    # data-qa="sibequkica">

    submit_button = driver.find_element(By.ID, "js-login-btn")
    submit_button.click()
    # Wait for sometime
    time.sleep(3)

    #<div
    # class="notification-box-description"
    # id="js-notification-box-msg"
    # data-qa="rixawilomi">
    # Your email, password, IP address or location did not match
    # </div>

    error_message_web_element = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message_web_element.text)

    assert error_message_web_element.text == os.getenv("ERROR_MESSAGE_EXPECTED")



    time.sleep(5)
    driver.quit()  # close everything.