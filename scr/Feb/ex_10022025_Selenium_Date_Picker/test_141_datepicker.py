
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
   # driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("05/30/2022") #mm/dd/yyyy

   year = "2028"
   month = "June"
   date = "30"

   driver.find_element(By.XPATH, "//*[@id='datepicker']").click()  # opens datepicker
   time.sleep(2)

   while True:
       mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
       yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

       if mon == month and yr == year:
           break;
       elif year > '2025':
           next_arrow=driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # Next arrow
       else:
           previous_arrow=driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() # Previous Arrow - old date

   # select date

   dates = driver.find_elements(By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

   for ele in dates:
       if ele.text == date:
           ele.click()
           break
   time.sleep(5)




