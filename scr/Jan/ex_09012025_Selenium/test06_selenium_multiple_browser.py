from selenium import webdriver
import pytest
import allure
import time


@allure.title("Verify the vwo.com title of the page")
def test_Katalon_Chrome():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found!!, Test Case Passed")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")
    time.sleep(10)


def test_Katalon_Edge():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found!!, Test Case Passed")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")
    time.sleep(10)


def test_Katalon_firefox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found!!, Test Case Passed")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")
    time.sleep(10)


# To run browsers parallely:
# pytest -n auto -s Selenium/Selenium_Basics/test06_selenium_multiple_browser.py