from selenium import webdriver
import pytest
import allure
import time


@allure.title("Verify the vwo.com title of the page")
def test_Katalon_Firebox():
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(10)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    driver.close()  # Closes the current window
    driver.quit()  # Quits the driver and closed every associated window