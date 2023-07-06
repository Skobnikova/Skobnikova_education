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
Button_Inner = driver.find_elements(By.XPATH, "//*[@class='ButtonInner-sc-14ud5tc-0 bABUvF encore-inverted-light-set']")
print(len(Button_Inner))
assert len(Button_Inner) > 0
