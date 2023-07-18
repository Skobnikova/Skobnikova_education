from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service('C:/path/to/chromedriver.exe'), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign In')]"))).click()
inputLogin = driver.find_element(By.ID, "signinEmail")
inputLogin.send_keys("annavolkova599@ukr.net")
inputPassword = driver.find_element(By.ID, "signinPassword")
inputPassword.send_keys("Gu21021970")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Login')]"))).click()
# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-primary:nth-child(2)"))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='dropdown-toggle user-nav_toggle']"))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='icon icon-instructions']"))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='icon icon-fuel']"))).click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@class='icon icon-logout']"))).click()
driver.close()

