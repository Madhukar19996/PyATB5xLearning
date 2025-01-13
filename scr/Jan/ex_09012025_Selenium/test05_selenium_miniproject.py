from selenium import webdriver
import pytest
import allure


@allure.title("Verify the CURA Healthcare Services title of the page")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURA Healthcare Service" in driver.page_source:
        print("Text Found!!, Test Case Passed")
    else:
        print("Text not found")


def test_vwo_sample1():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    if "CURE Healthcare Service" in driver.page_source:
        print("Text Found!!, Test Case Passed")
    else:
        print("Text not found on the page")
        pytest.fail("Text not found on the page")

#who closing the browser ?
# Python interpreter is closing the browser