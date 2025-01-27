from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    driver = webdriver.Edge()
    driver.get("https://awesomeqa.com/webtable1.html")
    # driver.maximize_window()

    # #Row
    # #//table[@id="customers"]/tbody/tr
    # row_elements= driver.find_elements(By.XPATH,"//table[@id='customers']/tbody/tr")
    # row = len(row_elements)
    # print(row)
    #
    # # Column
    # #//table[@id="customers"]/tbody/tr[2]/td
    # column_elements = driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[2]/td")
    # column = len (column_elements)
    # print(column)
    #
    # # 1st step-> //table[@id="customers"]/tbody/tr[
    # # 4 --> i (2,7)
    # #2nd step-> ]/td[
    # # 1 --> j (1,3)
    # #Third step-> ]
    #
    # first_part = "//table[@id='customers']/tbody/tr["
    # second_path = "]/td["
    # third_path ="]"
    # for i in range (2,row+1): # range(1,10) -> (1, 9+1)
    #     for j in range(1,column+1):
    #         dynamic_path =f"{first_part}{i}{second_path}{j}{third_path}"
    #         data = driver.find_element(By.XPATH, dynamic_path).text
    #
    #         #Find Helen Bannett's country
    #
    #         if "Helen Bennett" in data :
    #            country_path = f"{dynamic_path}/following-sibling::td"
    #            country_text = driver.find_element(By.XPATH,country_path).text
    #            print(f"Helen Bennett is in {country_text}")

    #
    # driver.get("https://awesomeqa.com/webtable1.html")
    # Get the table
    table = driver.find_element(By.XPATH, "//table[@summary='Sample Table']/tbody")
    row_table = table.find_elements(By.TAG_NAME, "tr")

    for row in row_table:
        column = row.find_elements(By.TAG_NAME, "td")
        for e in column:
            if "UAE" in e.text:
                print("Yes")

