# Automation for the Registration Page of the AwesomeQA.com/UI
#     Open - https://awesomeqa.com/ui/index.php?route=account/register
#     Fill the form
#     Verify that next page give - Your Account Has Been Created!
#------------------------------------------------------
from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
@allure.title("Opencart Registration Account Testing With Selenium_Mini_Project 3 ")
@allure.description("TC1 - Positive TC - Fill the registration form with Valid data and verify whether account created ")
@pytest.mark.Positive
def test_fill_reg_form():
    load_dotenv()
    driver=webdriver.Chrome()
    #Launch Opencart website
    driver.get(os.getenv("URL_OC"))
    time.sleep(5)
    ele_firstname = driver.find_element(By.XPATH,"//input[@name='firstname']")
    ele_firstname.send_keys(os.getenv("NAME_001_OC"))
    time.sleep(5)

    ele_lastname =driver.find_element(By.XPATH,"//input[@name='lastname']")
    ele_lastname.send_keys(os.getenv("LAST_NAME_001_OC"))
    time.sleep(5)


    ele_email = driver.find_element(By.XPATH,"//input[@name='email']")
    ele_email.send_keys(os.getenv("EMAIL_001_OC"))
    time.sleep(5)


    ele_phone = driver.find_element(By.XPATH,"//input[@name='telephone']")
    ele_phone.send_keys(os.getenv("TELEPHONE_001_OC"))
    time.sleep(5)




    ele_password = driver.find_element(By.XPATH,"//input[@name='password']")
    ele_password.send_keys(os.getenv("PASSWORD_001_OC"))
    time.sleep(5)


    ele_confirmPwd = driver.find_element(By.XPATH,"//input[@name='confirm']")
    ele_confirmPwd.send_keys(os.getenv("CONFIRM_PASSWORD_001_OC"))
    time.sleep(5)


    ele_policy_checkbox =driver.find_element(By.XPATH,"//input[@name='agree']")
    ele_policy_checkbox.click()
    time.sleep(3)

    ele_continue= driver.find_element(By.XPATH,"//input[@type='submit']")
    ele_continue.click()

    time.sleep(5)
    assert driver.current_url=="https://awesomeqa.com/ui/index.php?route=account/success"
    print(driver.title)
    time.sleep(6)
    driver.close()






@allure.title("Opencart Registration Account Testing With Selenium_Mini_Project 3 ")
@allure.description(
    "TC1 - Positive TC - Fill the registration form with Invalid data and verify whether account created ")
@pytest.mark.Positive
def test_fill_reg_form2():
    load_dotenv()
    driver = webdriver.Chrome()
    # Launch Opencart website
    driver.get(os.getenv("URL_OC"))
    time.sleep(5)
    ele_firstname = driver.find_element(By.XPATH, "//input[@name='firstname']")
    ele_firstname.send_keys(os.getenv("NAME_002_OC"))
    time.sleep(5)

    ele_lastname = driver.find_element(By.XPATH, "//input[@name='lastname']")
    ele_lastname.send_keys(os.getenv("LAST_NAME_002_OC"))
    time.sleep(5)

    ele_email = driver.find_element(By.XPATH, "//input[@name='email']")
    ele_email.send_keys(os.getenv("EMAIL_002_OC"))
    time.sleep(5)

    ele_phone = driver.find_element(By.XPATH, "//input[@name='telephone']")
    ele_phone.send_keys(os.getenv("TELEPHONE_002_OC"))
    time.sleep(5)

    ele_password = driver.find_element(By.XPATH, "//input[@name='password']")
    ele_password.send_keys(os.getenv("PASSWORD_002_OC"))
    time.sleep(5)

    ele_confirmPwd = driver.find_element(By.XPATH, "//input[@name='confirm']")
    ele_confirmPwd.send_keys(os.getenv("CONFIRM_PASSWORD_002_OC"))
    time.sleep(5)

    ele_policy_checkbox = driver.find_element(By.XPATH, "//input[@name='agree']")
    ele_policy_checkbox.click()
    time.sleep(3)

    ele_continue = driver.find_element(By.XPATH, "//input[@type='submit']")
    ele_continue.click()

    time.sleep(5)
    assert driver.current_url == "https://awesomeqa.com/ui/index.php?route=account/success"
    print(driver.title)
    time.sleep(8)
    driver.close()
    driver.quit()

