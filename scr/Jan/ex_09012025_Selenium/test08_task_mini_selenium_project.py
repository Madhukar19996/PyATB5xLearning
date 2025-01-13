from selenium import webdriver
import pytest
import allure
import time


@allure.title("Verify the demo.us.espocrm.com title of the page")
def test_demo_Edge():
    driver = webdriver.Edge()
    driver.get("https://demo.us.espocrm.com/")
    time.sleep(10)
    print(driver.title)
    assert driver.current_url == "https://demo.us.espocrm.com/"