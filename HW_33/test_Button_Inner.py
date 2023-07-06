from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# First test - expected result -> word "Results" should be on the page

options = Options()
options.add_argument("start-maximized")  # open Browser in maximized mode
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service("C:/path/to/chromedriver.exe"), options=options)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://open.spotify.com/")
# assert "Python_fail" in driver.title # Test fail
time.sleep(2)
# inputInner = driver.find_element(By.XPATH, "//*[@class='ButtonInner-sc-14ud5tc-0 bABUvF encore-inverted-light-set']")
# time.sleep(3)
# inputInner.send_keys(Keys.ENTER)
Inner = driver.find_element(By.XPATH,"//*[@class='ButtonInner-sc-14ud5tc-0 bABUvF encore-inverted-light-set']")

if Inner.is_displayed():
    print("Inner found")
    found = True
else:
    print("Inner not found")
    found = False

assert found