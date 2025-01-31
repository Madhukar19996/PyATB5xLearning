# 1) Count number of rows & columns
# 2) Read specific row & Column data
# 3) Read all the rows & Columns data
# 4) Read data based on condition(List books name whose author is Mukesh)


from selenium import webdriver
from selenium.webdriver.common.by import By


def test_web_tables():
    driver = webdriver.Edge()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()

    # Row
    # //table[@id="customers"]/tbody/tr
    row_elements = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
    row = len(row_elements)
    # print(row) #7

    # Column
    # //table[@name='BookTable']//tr/th
    column_elements = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr/th")
    column = len(column_elements)
    # print(column)#4

    # 2) Read specific row & Column data  - Master In Selenium

    data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
    # print(data)

    # 3) Read all the rows & Columns data

    # for r in range(2,row+1):
    #     for c in range(1,column+1):
    #         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
    #         print(data,end='   ')
    #     print()

    # 4) Read data based on condition(List books name whose author is Mukesh)

    for r in range(2, row + 1):
        authorName = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
        if authorName == "Mukesh":
            bookName = driver.find_element(By.XPATH,
                                           "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
            subject=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[3]").text
            price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
            print(bookName, " ", authorName, " ", subject," ", price," ")
        print()

    driver.close()
