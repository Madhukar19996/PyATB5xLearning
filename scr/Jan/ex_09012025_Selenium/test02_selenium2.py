from selenium import webdriver
import allure
import pytest
import time


@allure.title("Open the app .VWO.com")
@pytest.mark.regression
def test_VWO_Login():
    # 1. This code is translated into the API request
    # 2. POST request-Browser Driver (Server)
    # 3. Where it will create a Session or fresh copy Browser.(Chrome)
    # 4. Session ID - 16 digit (c4533a556af765ffcd1c9517fce2f4a7) will be created
    driver = webdriver.Chrome()
    print(driver.session_id)
    # 5. GET -> GET API request to navigate to particular page
    # 6. Browser will navigate to the URL
    # Source code(Client) -> API Request(W3C) -> Browser Driver(Server) -> Browser
    driver.get("https://app.vwo.com/")
    time.sleep(15)

