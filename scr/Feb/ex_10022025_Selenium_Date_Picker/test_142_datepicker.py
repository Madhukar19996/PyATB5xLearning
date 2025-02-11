from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_verify_date_picker():
   driver=webdriver.Chrome()
   driver.get("https://jqueryui.com/datepicker/")
   driver.maximize_window()

   driver.switch_to.frame(0)
   #  driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2022") #mm/dd/yyyy
   #
   # year = "2028"
   # month = "June"
   # date = "30"
   #
   # driver.find_element(By.XPATH, "//*[@id='datepicker']").click() # opens datepicker
   driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2028")

   time.sleep(5)
