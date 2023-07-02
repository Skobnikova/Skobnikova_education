from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os

absolute_path = os.path.dirname(__file__)
relative_path = "/"
full_path = os.path.join(absolute_path, relative_path)
print(f'Absolute Path: {absolute_path}')
print('Path:'+ full_path)

options = Options()
options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(absolute_path+'/chromedriver.exe'), options=options)

time.sleep(3)  # sleep for 3 sec
driver.get("https://dila.ua/")
# element = driver.find_element(By.ID, "contactsSection1")
# element = driver.find_element(By.XPATH, "//*[contains(text(),'Sign In')]")


element = driver.find_element(By.XPATH, "//*[@class='header-auth-btn header-help']")
if element.is_displayed():
    print("Element found")
    found = True
else:
    print("Element not found")
    found = False

assert found

driver.close()
