from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import re

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service('C:/path/to/chromedriver.exe'), options=options)

user = "guest"
password = "welcome2qauto"
driver.get("https://"+user+":"+password+"@"+"qauto2.forstudy.space/")
options.add_argument("start-maximized")

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class$='header_signin']"))).click()
inputLogin = driver.find_element(By.ID, "signinEmail")
inputLogin.send_keys("annavolkova599@ukr.net")
inputPassword = driver.find_element(By.ID, "signinPassword")
inputPassword.send_keys("Gu21021970")

class Test_Qauto_mix():
    def test_in_Login(self):
        in_Login = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary:nth-child(2)"))).click()
        assert 'in' in 'Login'

    def test_user_nav(self):

        user_nav = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[id^='u']"))).click()
        assert True

    def test_instr_icon(self):
        instr_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[class$='link -active']"))).get_attribute("class")
        assert len(instr_icon) > 0

    def test_fuel_icon(self):
        fuel_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[routerlink^='exp']"))).get_attribute("class")
        assert "class" != int

    def test_icon_logout(self):
        icon_logout = WebDriverWait(driver, 5).until( 
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[class*='danger']"))).get_attribute("class")
    assert "class" != "icon-logout"
    # driver.close()
