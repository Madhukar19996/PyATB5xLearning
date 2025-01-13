from selenium import webdriver
import pytest
import allure


@allure.title("Verify the vwo.com title of the page")
def test_vwo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)