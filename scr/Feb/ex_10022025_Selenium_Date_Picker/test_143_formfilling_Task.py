from selenium import webdriver
import allure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def test_verify_date_picker():
   driver=webdriver.Chrome()
   driver.get("https://fullclassnotes.blogspot.com/")
   driver.maximize_window()
   time.sleep(2)

   contactus_elm=driver.find_element(By.XPATH,"")
