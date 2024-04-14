from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import  Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import json
 
driver = webdriver.Firefox()
newRUL_list=[]

file = open("data.txt","r")

data = file.read()
file.close()
newRUL_list = data.split(",")


for i in range(len(newRUL_list)):
    driver.get(newRUL_list[i])
    try:
        time.sleep(random.randint(1,2))
        download_button = driver.find_element(By.ID,"downLoadFile")
        #download_button.click()
        time.sleep(random.randint(1,2))
        driver.execute_script("$(arguments[0]).click()",download_button)
        #webdriver.ActionChains(driver).move_to_element(download_button).click(download_button).perform()
    except:
        pass

    



