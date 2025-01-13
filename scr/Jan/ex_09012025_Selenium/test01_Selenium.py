from selenium import webdriver
import allure
import pytest
import time


@allure.title("Open the app .VWO.com")
@pytest.mark.regression
def test_VWO_Login():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com/")
    time.sleep(15)

