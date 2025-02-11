import time
from typing import Any

import pytest
import allure

from selenium import webdriver
from selenium.common import ElementNotVisibleException, NoSuchElementException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys


@allure.title("Opencart Registration Account Testing With Selenium_Mini_Project 3 ")
@allure.description("TC1 - Positive TC - Fill the registration form with Valid data and verify whether account created ")
@pytest.mark.Positive
def test_web_tables_status():


    driver = webdriver.Edge()
    driver.get("https://www.ultimatix.net/uxportal/uxportalhome.html/home")
    driver.maximize_window()
    # driver.implicitly_wait(10)  # seconds  # implicit wait


    # # Login
    user_id =driver.find_element(By.ID, "form1").send_keys("2252211")




    driver.find_element(By.XPATH, "//button[@id='proceed-button']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='easyAuth-btn']").click()
    time.sleep(15)

    # # # Admin-->user management-->users
    menu_button =driver.find_element(By.XPATH, "//div[@class='menuImgPage tooltips']").click()
    time.sleep(8)
    timesheet_button=driver.find_element(By.XPATH, "//a[@class='appLinksBlack ng-binding']").click()

    time.sleep(3)
    alldates=driver.find_elements(By.XPATH,"//table[@id='calenderTable']//td")

    for date_ele in alldates:
        date=date_ele.text()
        print(date)
        if date=="08":
            date_ele.click()
            break
    print(len(alldates))




    fill_working_hours=driver.find_element(By.XPATH, "(//input[@id='effortAssign00'])[1]").click()

    fill_working_hours.send_keys("8")
    time.sleep(3)

    summit_button= driver.find_element(By.XPATH, "//input[@id='datePickerLoadButton']").click()

    time.sleep(5)


    driver.close()




